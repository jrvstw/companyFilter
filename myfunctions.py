import sys
import re
import requests
import codecs
import fnmatch
import json
from bs4 import BeautifulSoup

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

def validate(argv):
    ieType = argv[1] if len(argv) > 1 else ""
    while re.search('^[EI]$', ieType) == None:
        ieType = input("I/E : ")
    ccc = argv[2] if len(argv) > 2 else ""
    while re.search('^[0-9]{4}$', ccc) == None:
        ccc = input("ccc : ")
    return (ieType, ccc)

def pageQuery(ieType, ccc, page):
    page_payload = 'state=queryAll&queryAllFlag=true&loginOlapId=&loginId=&loginRole=&loginName=&loginCompanyType=&loginRegUnitCode=&loginCaNo=&orderByColumn=&isAscending=true&progID=queryBasicf&filestoreLocation=D%3A%5CFileStore%5CFB&uploadKey=&q_BanNo=&q_CName=&q_EName=&q_Boss=&q_ieType=' + ieType + '&q_ccc=' + ccc + '&q_GoodName=&verifyCode=&currentPageSize=10&currentPage=' + str(page) + '&listContainerActiveRowId='
    return requests.request("POST", page_url, headers=page_headers, data = page_payload)

def basicQuery(number):
    basic_payload = "{\n    \"banNo\": \"" + number + "\"\n}"
    return requests.request("POST", basic_url, headers=basic_headers, data = basic_payload)

def gradeQuery(number):
    grade_payload = "{\n    \"banNo\": \"" + number + "\"\n}"
    return requests.request("POST", grade_url, headers=grade_headers, data = grade_payload)

def getCounts(ieType, ccc):
    src = pageQuery(ieType, ccc, 1)
    pagesCount = re.search('共(\d+)頁', src.text)[1]
    companiesCount = re.search('共(\d+)筆', src.text)[1]
    return int(pagesCount), int(companiesCount)

def getTable(ieType, ccc, page):
    response = pageQuery(ieType, ccc, str(page + 1))
    html = BeautifulSoup(response.text, "lxml")
    return html.find("section", attrs={"id":"listContainer"}).find_all("tr")[1:]

def getRow(ieType, ccc, page, index, company):
    serial = str(page * 10 + index + 1)
    number = company.find("a").string
    line = ieType + ',' + ccc + ',' + serial + ',"' + number + '"'

    response = basicQuery(number)
    data = json.loads(response.text)
    (name, area, address, phone) = ("", "", "", "")
    if data["result"] == "success":
        company = data["retrieveDataList"][0]
        name    = company[1]      if company[1] != None else ""
        area    = company[6][0:3] if company[6] != None else ""
        address = company[6]      if company[6] != None else ""
        phone   = company[8]      if company[8] != None else ""
    line += ',' + name + ',' + area + ',' + address + ',"' + phone + '"'

    response = gradeQuery(number)
    data = json.loads(response.text)
    companys = data["retrieveDataList"]
    if data["result"] == "success":
        for company in companys:
            line += ',' + company[4] + ',' + company[5]

    return line

