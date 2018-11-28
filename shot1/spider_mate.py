import requests
import json
import bs4
import cx_Oracle       #引用模块cx_Oracle
import readbak
import openpyxl
import numpy as np
import re
import creat_html

jason_filename = 'result.json'

def conORCL():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')    #连接数据库
    return conn

def closORCL():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')    #连接数据库
    c = conn.cursor()
    c.close()  # 关闭cursor
    conn.close()

def wjson(results):
    data = np.empty((len(results), 3))
    with open(jason_filename, "w", encoding="utf-8") as js:
        js.write('{"result":[')
        i = 0
        j = len(results)
        for result in range(0, j):

            url = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", results[0][1])
            url = str(url).strip('[]').strip("'")

            js.write('{"name":"'+ results[result][0]+'",\r\n')
            js.write('"url":"'+ url+'",\r\n')
            if i == j-1:
                js.write('"y/n":"'+ '未知"}'+'\r\n')
            else :
                js.write('"y/n":"' + '未知"},' + '\r\n')
            i=i+1
        js.write(']\r\n}')
            # res = get_url(url)
            # on_or_not = findata(res)
    # fdata = np.c_[results, data]
    return data

def to_excel(data):
    wb = openpyxl.workbook()
    wb.guss_type = True
    ws = wb.active
    ws.append(['名字', '地址', '是否在线'])
    for each in data:
        ws.append(each)
    ws.save("大香蕉结果集.xlsx")



def is_online(res):
    netjson = json.loads(res.text)
    online_or_not = netjson['nowpage']
    with open('is_online.txt', 'w', encoding='utf-8') as file:
        for each in online_or_not:
            file.write(each)

def findata(res):#查找是否在线并返回数字 isonline
    date = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find("span", class_="nowpage")
    a = re.search('.',content.string)
    is_or_not = a.string.strip().find("休息")
    return is_or_not


def get_url(url):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    return res

def ask(url):
    res = get_url(url)
    num = findata(res)
    if num > 0:
        answer = "不在线"
    else:
        answer = "在线"
    return answer

def read_url(path):
    with open(jason_filename, encoding="utf-8") as js:
        result = json.loads(js.read())
        i = 0
        for re in result['result']:
            is_or_not = ask(result['result'][i]['url'])
            result['result'][i]['y/n'] = is_or_not
            i = 1 + i

    with open(jason_filename, "w", encoding="utf-8") as js:
        json.dump(result, js, ensure_ascii=False)

def main():
    result = readbak.readjson()
    wjson(result)
    read_url(jason_filename)
    print("Over")

if __name__ == '__main__':
    main()
