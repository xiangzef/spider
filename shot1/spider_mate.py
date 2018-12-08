import requests
import json
import bs4
import cx_Oracle       #引用模块cx_Oracle
import readbak
#from tools.is_old import is_old
import time
# import openpyxl
import numpy
import re
import MyThreat
import creat_html as h5
#pip install Pyinstaller
#打包语句

rate = 0
jason_filename = '../file/result.json'


def conORCL():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')    #连接数据库
    return conn


def closORCL():
    conn = cx_Oracle.connect('FD20180816/FD20180816@ORCL')    #连接数据库
    c = conn.cursor()
    c.close()  # 关闭cursor
    conn.close()
    return 1


def wjson(results, path):
    with open(path, "w", encoding="utf-8") as js:
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
            else:
                js.write('"y/n":"' + '未知"},' + '\r\n')
            i = i+1
        js.write(']\r\n}')
    return 1


# def to_excel(data):
#     wb = openpyxl.workbook()
#     wb.guss_type = True
#     ws = wb.active
#     ws.append(['名字', '地址', '是否在线'])
#     for each in data:
#         ws.append(each)
#     ws.save("大香蕉结果集.xlsx")
#     return 1


def is_online(res):
    netjson = json.loads(res.text)
    online_or_not = netjson['nowpage']
    with open('is_online.txt', 'w', encoding='utf-8') as file:
        for each in online_or_not:
            file.write(each)
    return 1


def findata(res):#查找是否在线并返回数字 isonline
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find("span", class_="nowpage")
    if content is None:
        return '错误链接',-2
    else:
        a = re.search('.', content.string).string
        is_or_not = a.string.strip().find("休息")
        return a, is_or_not


def get_url(url):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    if url.strip().find('du672') >0:
        res = requests.get(url, headers=headers)
        return res


def ask(url):
    if url.strip().find('du672') < 0:
        answer = "错误链接"
        name = "错误连接"
    else:
        res = get_url(url)
        num = findata(res)
        name = num[0]
        if num[1] > 0:
            answer = "不在线"
        elif num[1] == -1:
            answer = "在线"
        else:
            answer = "错误链接"
    return answer, name


def read_url(path):
    global rate
    with open(path, encoding="utf-8") as js:
        result = json.loads(js.read())
        i = 0
        rate = round(len(result['result']) / 7)
        lst = numpy.arange(1, len(result['result']), 1)
        new_list = list(newlist(lst))
        for res in result['result']:
            MyThreat.call_thr(i, res, new_list, len(result['result']))
            i = 1 + i
        MyThreat.start_thr(result)
    with open(path, "w", encoding="utf-8") as js:
        json.dump(result, js, ensure_ascii=False)


def is_odd(n):
    global rate
    y = rate
    return n % y == 0


def newlist(lst):
    newlist = filter(is_odd, lst)
    return newlist


def execute(parameter):
    if parameter == 1:
        # 读取 book 生成 结果
        # 利用结果生成json
        readbak.readbak()
        results = readbak.readjson()
        wjson(results, jason_filename)
        # 读 file\result.json 查询网页 更新 y/n 生成网页并打开
        read_url(jason_filename)
        h5.html_auto()
    else:
        # 只生产html文件
        h5.html_auto()

def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    execute(1)
    print("100%")
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


if __name__ == '__main__':
    main()
