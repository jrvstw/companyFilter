import json

text = '{"result":"success","retrieveDataList":[["28615990","109   01-05","今勝機械有限公司","CHIEN SHIENG MACHINERY CO., LTD.","M","L","109"],["28615990","108   01-12","今勝機械有限公司","CHIEN SHIENG MACHINERY CO., LTD.","M","L","108"],["28615990","107   01-12","今勝機械有限公司","CHIEN SHIENG MACHINERY CO., LTD.","L","L","107"],["28615990","106   01-12","今勝機械有限公司","CHIEN SHIENG MACHINERY CO., LTD.","M","L","106"],["28615990","105   01-12","今勝機械有限公司","CHIEN SHIENG MACHINERY CO., LTD.","L","L","105"]],"viewmodel":{"banNo":"28615990"}}'
data = json.loads(text)

if not data["result"] == "success":
    exit()

company = data["retrieveDataList"]
print(company[0][0], company[0][2])
print(company[0][6], company[0][4], company[0][5])
print(company[1][6], company[1][4], company[1][5])
print(company[2][6], company[2][4], company[2][5])
print(company[3][6], company[3][4], company[3][5])
print(company[4][6], company[4][4], company[4][5])

