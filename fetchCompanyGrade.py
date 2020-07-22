import requests
import json
#from time import gmtime, strftime

cookie =  'JSESSIONID=djXF9K0VwicVaTL8-8rUTQFkfW1H8L1MBvwkLH8Q.fbfhweb; TS014088ba=01ce097c29e128d89060a67b19fcb75aa7005c891aba61c7cc5c01af402452d4df26e76e6c783fba575af48dcda860f7e4dd51fddcd2ead32aaa3187010a951150dfe02d46; ASP.NET_SessionId=dmryamltuybubsuyse2porjb; TS017243ec=01ce097c290265730f6b687dbb2e6cafeae2424c814bc11b3dbc923d9bc3bc8d1cbd2c27867994d518d9a0821f32da7c02a9b7f4a7d8e4d87832de18e2f054d0744186d7cc; TS01f995a3=01ce097c29d3b317a666a49834fabd03013d8644e593aee854fdfbd376cb519fd8138616820e27f900647355b493cc61d546013550; TS01f995a3=01ce097c29c17c2fcb90b28ccdb69fa363cbff8c7713c7ad1c6fa23e7b2fec495aa78505221394b3fc4acaee0ecdf1d5d8482da69e'
taxNumbers = [
        "12341051"
        ]
'''
        "13016650",
        "29178716",
        "89481488",
        "16258785",
        "16997966",
        "53715933",
        "80095345",
        "25723123",
        "97194093",
        "28615990"
        "24602381" # forbidden
        ]
'''


url = "https://fbfh.trade.gov.tw/fb/common/popGrade.action"
headers = {
  'Cookie':cookie,
  'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'https://fbfh.trade.gov.tw',
  'referer': 'https://fbfh.trade.gov.tw/fb/web/queryBasicf.do',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
 #'Date': strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
}

for taxNumber in taxNumbers:
    payload = "{\n    \"banNo\": \"" + taxNumber + "\"\n}"
    response = requests.request("POST", url, headers=headers, data = payload)
    data = json.loads(response.text)

    if not data["result"] == "success":
        continue

    company = data["retrieveDataList"]
    print(company[0][0], company[0][2])
    print(company[0][6], company[0][4], company[0][5])
    print(company[1][6], company[1][4], company[1][5])
    print(company[2][6], company[2][4], company[2][5])
    print(company[3][6], company[3][4], company[3][5])
    print(company[4][6], company[4][4], company[4][5])

    #print(response.text) #.encode('utf8'))

