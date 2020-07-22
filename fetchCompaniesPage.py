import requests

q_ieType = 'E'
q_ccc    = '8504'
q_page   = '416'

cookie = 'JSESSIONID=6y1sC6IltAB39vU73l3L704bBXW7FmDaBnz7zjpd.fbfhweb; TS014088ba=01ce097c29b7c424c2aa417979661e0552a52dca3fba61c7cc5c01af402452d4df26e76e6c783fba575af48dcda860f7e4dd51fddc45bba160e0c9c856888c8de0ccf70f4c; ASP.NET_SessionId=dmryamltuybubsuyse2porjb; TS017243ec=01ce097c290265730f6b687dbb2e6cafeae2424c814bc11b3dbc923d9bc3bc8d1cbd2c27867994d518d9a0821f32da7c02a9b7f4a7d8e4d87832de18e2f054d0744186d7cc; TS01f995a3=01ce097c29769ba2d842d236474a70ed4694c02839953759f8e8294cb49cb57e73d90f512423bf07b1ba15220937e154709b5591c5'

url = "https://fbfh.trade.gov.tw/fb/web/queryBasicf.do"
payload = 'state=queryAll&queryAllFlag=true&loginOlapId=&loginId=&loginRole=&loginName=&loginCompanyType=&loginRegUnitCode=&loginCaNo=&orderByColumn=&isAscending=true&progID=queryBasicf&filestoreLocation=D%3A%5CFileStore%5CFB&uploadKey=&q_BanNo=&q_CName=&q_EName=&q_Boss=&q_ieType=' + q_ieType + '&q_ccc=' + q_ccc + '&q_GoodName=&verifyCode=&currentPageSize=10&currentPage=' + q_page + '&listContainerActiveRowId='
headers = {
  'Cache-Control': 'max-age=0',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
response = requests.request("POST", url, headers=headers, data = payload)

print(response.text) #.encode('utf8'))

