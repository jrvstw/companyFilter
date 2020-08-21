import sys
import re
import requests
import codecs
import fnmatch
import json
from bs4 import BeautifulSoup

# 以下為向伺服器發送請求所需的資料
# 這些資料有可能因伺服器內部更動而需要更新
cookie = 'JSESSIONID=6y1sC6IltAB39vU73l3L704bBXW7FmDaBnz7zjpd.fbfhweb; TS014088ba=01ce097c29b7c424c2aa417979661e0552a52dca3fba61c7cc5c01af402452d4df26e76e6c783fba575af48dcda860f7e4dd51fddc45bba160e0c9c856888c8de0ccf70f4c; ASP.NET_SessionId=dmryamltuybubsuyse2porjb; TS017243ec=01ce097c290265730f6b687dbb2e6cafeae2424c814bc11b3dbc923d9bc3bc8d1cbd2c27867994d518d9a0821f32da7c02a9b7f4a7d8e4d87832de18e2f054d0744186d7cc; TS01f995a3=01ce097c29785ba83d608149215a9fa09e57937658e12625e16383ed4f11b9180d0bbcc177c7f8f75485522968c256ef161248d342'
userAgent =  'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

page_url = "https://fbfh.trade.gov.tw/fb/web/queryBasicf.do"
page_headers = {
  'Cache-Control': 'max-age=0',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent':userAgent,
  'Origin': 'https://fbfh.trade.gov.tw',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'Referer': 'https://fbfh.trade.gov.tw/fb/web/queryBasicf.do',
  'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
  'Cookie': cookie,
  'Content-Type': 'application/x-www-form-urlencoded'
}

basic_url = "https://fbfh.trade.gov.tw/fb/common/popBasic.action"
basic_headers = {
  'Cookie':cookie,
  'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'https://fbfh.trade.gov.tw',
  'referer': 'https://fbfh.trade.gov.tw/fb/web/queryBasicf.do',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent':userAgent,
  'X-Requested-With': 'XMLHttpRequest'
}

grade_url = "https://fbfh.trade.gov.tw/fb/common/popGrade.action"
grade_headers = basic_headers

# 向伺服器送出「查詢某稅則的某頁」的請求
def pageQuery(ieType, ccc, page):
    page_payload = 'state=queryAll&queryAllFlag=true&loginOlapId=&loginId=&loginRole=&loginName=&loginCompanyType=&loginRegUnitCode=&loginCaNo=&orderByColumn=&isAscending=true&progID=queryBasicf&filestoreLocation=D%3A%5CFileStore%5CFB&uploadKey=&q_BanNo=&q_CName=&q_EName=&q_Boss=&q_ieType=' + ieType + '&q_ccc=' + ccc + '&q_GoodName=&verifyCode=&currentPageSize=10&currentPage=' + str(page) + '&listContainerActiveRowId='
    return requests.request("POST", page_url, headers=page_headers, data = page_payload)

# 向伺服器送出「查詢某公司基本資料」的請求
def basicQuery(number):
    basic_payload = "{\n    \"banNo\": \"" + number + "\"\n}"
    return requests.request("POST", basic_url, headers=basic_headers, data = basic_payload)

# 向伺服器送出「查詢某公司近五年實績」的請求
def gradeQuery(number):
    grade_payload = "{\n    \"banNo\": \"" + number + "\"\n}"
    return requests.request("POST", grade_url, headers=grade_headers, data = grade_payload)

# 查詢某稅則下有多少頁
def getPagesCount(ieType, ccc):
    src = pageQuery(ieType, ccc, 1)
    pagesCount = re.search('共(\d+)頁', src.text)[1]
    return int(pagesCount)

# 查詢某稅則下有多少筆公司資料
def getCompaniesCount(ieType, ccc):
    src = pageQuery(ieType, ccc, 1)
    companiesCount = re.search('共(\d+)筆', src.text)[1]
    return int(companiesCount)

# 抓取某頁中的公司列表
def getTable(ieType, ccc, page):
    response = pageQuery(ieType, ccc, str(page + 1))
    html = BeautifulSoup(response.text, "lxml")
    return html.find("section", attrs={"id":"listContainer"}).find_all("tr")[1:]

# 抓取某稅則的公司統編列表
def getCategory(outfile, ieType, ccc, mode = ""):
    with open(outfile, 'w') as f:
        header = '進出口,稅則,序號,統編'
        header = '"I/E",ccc,serial,"tax number"'
        f.write(header + '\n')
        for page in range(getPagesCount(ieType, ccc)):
            table = getTable(ieType, ccc, page)
            for index, company in enumerate(table):
                serial = page * 10 + index + 1
                number = company.find("a").string
                row = f'{ieType},{ccc},{serial},{number}'
                if mode != "d":
                    f.write(row + '\n')
                print(row)

# 抓取某公司的基本資料
def getCompanyBasic(number):
    number = str(number).zfill(8)
    basic = {
            '統編': number,
            }
    response = basicQuery(number)
    data = json.loads(response.text)
    if data["result"] == "success":
        company = data["retrieveDataList"][0]
        basic['公司名']       = company[1]      if company[1] != None else ""
        basic['登記日']   = company[4]      if company[4] != None else ""
        basic['城市']       = company[6][0:3] if company[6] != None else ""
        basic['地址']    = company[6]      if company[6] != None else ""
        basic['電話']      = company[8]      if company[8] != None else ""

        if basic['登記日'] != "":
            date = basic['登記日'].split('/')
            date[0] = str(int(date[0]) + 1911)
            basic['登記日'] = '-'.join(date)
    return basic

# 抓取某公司的近五年實績
# 注意：不同年份的資料在合併時，要確認同欄位是否同年份
def getCompanyGrade(number):
    number = str(number).zfill(8)
    grade = {
            '統編': number,
            }
    response = gradeQuery(number)
    data = json.loads(response.text)
    company = data["retrieveDataList"]
    if data["result"] == "success":
        for entry in company[:5]:
            grade['i' + entry[6]] = entry[4]
            grade['e' + entry[6]] = entry[5]
    return grade

