from bs4 import BeautifulSoup
import requests
import codecs
import os
import fnmatch

infile = "infiles/htmls"
outfile = "outfiles/ImpExpValues.csv"
fp = open(outfile, "w")

for category in os.listdir(infile):
    subdir = infile + '/' + category
    if not os.path.isdir(subdir):
        continue

    for filename in os.listdir(subdir):
        if not fnmatch.fnmatch(filename, '*.html'):
            continue
        filepath = subdir + '/' + filename

        #html_content = requests.get(filepath).text
        html_content = codecs.open(filepath, 'r', encoding="utf-8")
        page = BeautifulSoup(html_content, "lxml")
        table = page.find("tbody", attrs={"id":"kdbase_popGradeList"})

        taxNumber = page.find("span", attrs={"id":"banNoM2"}).span.text
        imp = []
        exp = []
        for tr in table.find_all("tr"):
            td = tr.find_all("td")
            imp.append(td[1].text)
            exp.append(td[2].text)

        row = taxNumber + ',' + category + ',' + filename + ',' + ','.join(imp) + ',' + ','.join(exp) + '\n'
        print(row)
        fp.write(row)

fp.close()

