import requests
from bs4 import BeautifulSoup
import json


URLs = ["https://seesaawiki.jp/imascg/d/%BF%B9%B5%D7%CA%DD%C7%B5%A1%B9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%e1%a5%eb%a5%d8%a5%f3%a1%f5%a5%b4%a5%b7%a5%c3%a5%af%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%cd%a5%ac%a5%c6%a5%a3%a5%f4%b2%b5%bd%f7%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%cf%a5%ed%a5%a6%a5%a3%a5%f3%a5%ca%a5%a4%a5%c8%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a4%aa%a4%c9%a4%aa%a4%c9%bc%ed%bf%cd%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%cc%c2%a1%b9%a5%a8%a5%b9%a5%b1%a1%bc%a5%d7%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%e1%a5%eb%a5%d8%a5%f3%a5%d6%a5%c3%a5%af%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%a4%a1%bc%a5%b9%a5%bf%a1%bc%a5%cf%a5%d7%a5%cb%a5%f3%a5%b0%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%a8%a5%b9%a5%b1%a1%bc%a5%d7%a5%d6%a5%e9%a5%a4%a5%c9%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%b5%a5%de%a1%bc%a5%ea%a5%be%a1%bc%a5%c8%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        ]


all_speeches = []

for url in URLs:
    # GETリクエスト
    response = requests.get(url)
    print(response.status_code)
    print(response.reason)
    response.raise_for_status() #ステータスコードが200番台以外なら例外起こす．

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all("table")
    speeches = [] #台詞のリスト
    # 特訓前セリフ---------------------------------------------
    table = elements[2]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    speeches.append(rows[2].find_all("td")[1].text)
    speeches.append(rows[3].find_all("td")[0].text)
    speeches.append(rows[4].find_all("td")[0].text)
    speeches.append(rows[5].find_all("td")[0].text)
    speeches.append(rows[7].find_all("td")[1].text)
    speeches.append(rows[8].find_all("td")[0].text)
    speeches.append(rows[9].find_all("td")[0].text)
    speeches.append(rows[10].find_all("td")[0].text)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓前セリフ---------------------------------------------


    # 特訓後セリフ---------------------------------------------
    table = elements[5]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    s = rows[2].find_all("td")[1].text
    if not s in speeches: #被りはスルー
        speeches.append(s)
    for i in range(3,6):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    s = rows[7].find_all("td")[1].text
    if not s in speeches:
        speeches.append(s)
    for i in range(8,11):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓後セリフ---------------------------------------------

    title = soup.select('.title')[0].text
    print(title)
    for s in speeches:
        print(s)

    all_speeches.extend(speeches)
    print(len(all_speeches))



# ----------------------テーブルの形が違うもの１----------------------
URLs = [
        "https://seesaawiki.jp/imascg/d/%a1%ce%ba%a4%cf%c7%a4%ce%be%ae%a5%ea%a5%b9%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        ]

for url in URLs:
    # GETリクエスト
    response = requests.get(url)
    print(response.status_code)
    print(response.reason)
    response.raise_for_status() #ステータスコードが200番台以外なら例外起こす．

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all("table")
    speeches = [] #台詞のリスト
    # 特訓前セリフ---------------------------------------------
    table = elements[2]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[5].find_all("td")[1].text)
    speeches.append(rows[6].find_all("td")[1].text)
    speeches.append(rows[7].find_all("td")[0].text)
    speeches.append(rows[8].find_all("td")[0].text)
    speeches.append(rows[9].find_all("td")[0].text)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[0].text)
    speeches.append(rows[13].find_all("td")[0].text)
    speeches.append(rows[14].find_all("td")[0].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    speeches.append(rows[18].find_all("td")[1].text)
    speeches.append(rows[19].find_all("td")[1].text)
    speeches.append(rows[20].find_all("td")[1].text)
    # 特訓前セリフ---------------------------------------------


    # 特訓後セリフ---------------------------------------------
    table = elements[5]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    s = rows[2].find_all("td")[1].text
    if not s in speeches: #被りはスルー
        speeches.append(s)
    for i in range(3,6):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    s = rows[7].find_all("td")[1].text
    if not s in speeches:
        speeches.append(s)
    for i in range(8,11):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓後セリフ---------------------------------------------

    title = soup.select('.title')[0].text
    print(title)
    for s in speeches:
        print(s)

    all_speeches.extend(speeches)
    print(len(all_speeches))

# ----------------------テーブルの形が違うもの１----------------------


# ----------------------テーブルの形が違うもの２----------------------
URLs = [
        "https://seesaawiki.jp/imascg/d/%a1%ce%be%ae%a4%b5%a4%ca%a4%ab%a4%af%a4%ec%a4%f3%a4%dc%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%db%a5%ef%a5%a4%a5%c8%a5%a2%a5%a6%a5%c8%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%b7%a5%f3%a5%c7%a5%ec%a5%e9%a5%c9%a5%ea%a1%bc%a5%e0%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        "https://seesaawiki.jp/imascg/d/%a1%ce%cc%b4%a4%ce%a4%b5%a4%b5%a4%e4%a4%ad%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        ]

for url in URLs:
    # GETリクエスト
    response = requests.get(url)
    print(response.status_code)
    print(response.reason)
    response.raise_for_status() #ステータスコードが200番台以外なら例外起こす．

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all("table")
    speeches = [] #台詞のリスト
    # 特訓前セリフ---------------------------------------------
    table = elements[2]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[3].find_all("td")[1].text)
    speeches.append(rows[4].find_all("td")[1].text)
    speeches.append(rows[5].find_all("td")[0].text)
    speeches.append(rows[6].find_all("td")[0].text)
    speeches.append(rows[7].find_all("td")[0].text)
    speeches.append(rows[9].find_all("td")[1].text)
    speeches.append(rows[10].find_all("td")[0].text)
    speeches.append(rows[11].find_all("td")[0].text)
    speeches.append(rows[12].find_all("td")[0].text)
    speeches.append(rows[13].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    speeches.append(rows[17].find_all("td")[1].text)
    speeches.append(rows[18].find_all("td")[1].text)
    # 特訓前セリフ---------------------------------------------


    # 特訓後セリフ---------------------------------------------
    table = elements[5]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    s = rows[2].find_all("td")[1].text
    if not s in speeches: #被りはスルー
        speeches.append(s)
    for i in range(3,6):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    s = rows[7].find_all("td")[1].text
    if not s in speeches:
        speeches.append(s)
    for i in range(8,11):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓後セリフ---------------------------------------------

    title = soup.select('.title')[0].text
    print(title)
    for s in speeches:
        print(s)

    all_speeches.extend(speeches)
    print(len(all_speeches))

# ----------------------テーブルの形が違うもの２----------------------


# ----------------------テーブルの形が違うもの３----------------------
URLs = [
        "https://seesaawiki.jp/imascg/d/%a1%ce%a5%b7%a5%e7%a5%b3%a5%e9%a5%d0%a5%ec%a5%f3%a5%bf%a5%a4%a5%f3%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        ]

for url in URLs:
    # GETリクエスト
    response = requests.get(url)
    print(response.status_code)
    print(response.reason)
    response.raise_for_status() #ステータスコードが200番台以外なら例外起こす．

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all("table")
    speeches = [] #台詞のリスト
    # 特訓前セリフ---------------------------------------------
    table = elements[3]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[6].find_all("td")[1].text)
    speeches.append(rows[7].find_all("td")[1].text)
    speeches.append(rows[8].find_all("td")[0].text)
    speeches.append(rows[9].find_all("td")[0].text)
    speeches.append(rows[10].find_all("td")[0].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[13].find_all("td")[0].text)
    speeches.append(rows[14].find_all("td")[0].text)
    speeches.append(rows[15].find_all("td")[0].text)
    speeches.append(rows[16].find_all("td")[1].text)
    speeches.append(rows[17].find_all("td")[1].text)
    speeches.append(rows[19].find_all("td")[1].text)
    speeches.append(rows[20].find_all("td")[1].text)
    speeches.append(rows[21].find_all("td")[1].text)
    # 特訓前セリフ---------------------------------------------


    # 特訓後セリフ---------------------------------------------
    table = elements[7]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    s = rows[2].find_all("td")[1].text
    if not s in speeches: #被りはスルー
        speeches.append(s)
    for i in range(3,6):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    s = rows[7].find_all("td")[1].text
    if not s in speeches:
        speeches.append(s)
    for i in range(8,11):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓後セリフ---------------------------------------------

    title = soup.select('.title')[0].text
    print(title)
    for s in speeches:
        print(s)

    all_speeches.extend(speeches)
    print(len(all_speeches))

# ----------------------テーブルの形が違うもの３----------------------


# ----------------------テーブルの形が違うもの４----------------------
URLs = [
        "https://seesaawiki.jp/imascg/d/%a1%ce6th%a5%a2%a5%cb%a5%d0%a1%bc%a5%b5%a5%ea%a1%bc%a1%cf%bf%b9%b5%d7%ca%dd%c7%b5%a1%b9",
        ]

for url in URLs:
    # GETリクエスト
    response = requests.get(url)
    print(response.status_code)
    print(response.reason)
    response.raise_for_status() #ステータスコードが200番台以外なら例外起こす．

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all("table")
    speeches = [] #台詞のリスト
    # 特訓前セリフ---------------------------------------------
    table = elements[3]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    speeches.append(rows[2].find_all("td")[1].text)
    speeches.append(rows[3].find_all("td")[0].text)
    speeches.append(rows[4].find_all("td")[0].text)
    speeches.append(rows[5].find_all("td")[0].text)
    speeches.append(rows[7].find_all("td")[1].text)
    speeches.append(rows[8].find_all("td")[0].text)
    speeches.append(rows[9].find_all("td")[0].text)
    speeches.append(rows[10].find_all("td")[0].text)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓前セリフ---------------------------------------------


    # 特訓後セリフ---------------------------------------------
    table = elements[7]
    # print(table)
    rows = table.find_all("tr")
    speeches.append(rows[1].find_all("td")[1].text)
    s = rows[2].find_all("td")[1].text
    if not s in speeches: #被りはスルー
        speeches.append(s)
    for i in range(3,6):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    s = rows[7].find_all("td")[1].text
    if not s in speeches:
        speeches.append(s)
    for i in range(8,11):
        s = rows[i].find_all("td")[0].text
        if not s in speeches:
            speeches.append(s)
    speeches.append(rows[11].find_all("td")[1].text)
    speeches.append(rows[12].find_all("td")[1].text)
    speeches.append(rows[14].find_all("td")[1].text)
    speeches.append(rows[15].find_all("td")[1].text)
    speeches.append(rows[16].find_all("td")[1].text)
    # 特訓後セリフ---------------------------------------------

    title = soup.select('.title')[0].text
    print(title)
    for s in speeches:
        print(s)

    all_speeches.extend(speeches)
    print(len(all_speeches))

# ----------------------テーブルの形が違うもの４----------------------


with open("./speeches_morikubo.txt",mode='a') as f:
    for s in all_speeches:
        f.write(s+"\n")
