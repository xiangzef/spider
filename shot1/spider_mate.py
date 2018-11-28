import requests
import json
import bs4
import cx_Oracle       #引用模块cx_Oracle
import readbak
import openpyxl
import numpy as np
import re
import creat_html as h5

jason_filename = '../file/result.json'

def conORCL():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')    #连接数据库
    return conn

def closORCL():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')    #连接数据库
    c = conn.cursor()
    c.close()  # 关闭cursor
    conn.close()

def wjson(results):
    with open(jason_filename, "w", encoding="utf-8") as js:
        js.write('{"result":[')
        i = 0
        j = len(results)
        for result in range(0, j):

            url = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", results[i][1])
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
    if content is None:
        return -1
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
    elif num == 0:
        answer = "在线"
    else:
        answer = "错误链接"
    return answer

def read_url(path):
    with open(jason_filename, encoding="utf-8") as js:
        result = json.loads(js.read())
        i = 0
        for re in result['result']:
            if re['y/n'] is not "错误链接":
                is_or_not = ask(result['result'][i]['url'])
            result['result'][i]['y/n'] = is_or_not
            i = 1 + i

    with open(jason_filename, "w", encoding="utf-8") as js:
        json.dump(result, js, ensure_ascii=False)

def main():
    #读取 book 生成 结果
    #利用结果生成json

    # result = readbak.readjson()
    # wjson(result)

    #读 file\result.json 查询网页 更新 y/n 生成网页并打开
    read_url(jason_filename)
    print("Over")
    h5.html_auto()


if __name__ == '__main__':
    main()
