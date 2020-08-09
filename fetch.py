import sys
import os
import re

# fbfhTools.py: 自建的「出進口廠商管理系統」網頁的工具包
#   |- getCompaniesCount: 查詢該稅則下有多少筆公司資料
#   |- getCategory:       抓取該稅則的公司統編列表
from fbfhTools import getCompaniesCount
from fbfhTools import getCategory

# validate:
#   驗證輸入參數的格式。程式所需參數可由程式提示或於命令列輸入。
#   直接執行本程式，會出現以下提示：
#
#       Category:
#
#   在提示後輸入稅則，範例如下：
#
#       Category: E8502
#
#   若非直接執行，而是使用命令列，其指令範例如下：
#
#       > python fetch.py E8502
#
#   若格式錯誤，則會提示輸入稅則。其輸入方法可參照前例。
#   命令列輸入允許額外參數，例如：
#
#       > python fetch.py E8502 y
#
#   參數"y"可避開所有輸入提示，以滿足自動化需求。
#   另一參數"d"為測試用，不實際寫入檔案，只顯示於螢幕：
#
#       > python fetch.py E8502 d
#
def validate(argv):
    category = argv[1] if len(argv) > 1 else ""
    mode     = argv[2] if len(argv) > 2 else ""
    if re.search('^[EI][0-9]{4}$', category) == None:
        if mode == "y":
            exit(f"Failed: {category}")
        category = input("Category : ")
        while re.search('^[EI][0-9]{4}$', category) == None:
            print("Invalid input.")
            category = input("Category : ")
    return (category[0], category[1:], mode)

# 1. 驗證輸入、決定輸出檔名
(ieType, ccc, mode) = validate(sys.argv)
companiesCount = getCompaniesCount(ieType, ccc)
outfile = f"outfiles{os.path.sep}{ieType}{ccc}_{companiesCount}.csv"

# 2. 經使用者確認，才可執行，除非為 y 或 d 模式
if mode not in ["y", "d"]:
    print(f"Saving {companiesCount} items to '{outfile}'.")
    if input("Enter 'y' to proceed: ") != "y":
        exit("Abort.")

# 3. 抓取該稅則下所有公司統編
getCategory(outfile, ieType, ccc, mode)

