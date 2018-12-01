import requests
import json
import bs4
import cx_Oracle       #引用模块cx_Oracle
import readbak
# import openpyxl
# import numpy as np
import re
import creat_html as h5

#pip install Pyinstaller
#打包语句


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


def wjson(results,path):
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
    if url.strip().find('du871') >0:
        res = requests.get(url, headers=headers)
        return res


def ask(url):
    if url.strip().find('du871') < 0:
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
    with open(path, encoding="utf-8") as js:
        result = json.loads(js.read())
        i = 0
        for res in result['result']:
            if res['y/n'] is not "错误链接":
                answer_name = ask(result['result'][i]['url'])
            result['result'][i]['y/n'] = answer_name[0]
            if str(answer_name[0]).strip() == '在线' and str(result['result'][i]['name']).strip() == '大香蕉直播間_全球美女直播_大香蕉伊人網_大香蕉网_伊人在线大香蕉' :
                result['result'][i]['name'] = re.findall(r'[0-9a-zA-z_]+',str(answer_name[1]).strip().strip('\n'))[0]#正则表达式匹配大小写字母数字和下划线
            i = 1 + i

    with open(path, "w", encoding="utf-8") as js:
        json.dump(result, js, ensure_ascii=False)

def main():
    #读取 book 生成 结果
    #利用结果生成json
    readbak.readbak()
    result = readbak.readjson()
    wjson(result, jason_filename)
    #读 file\result.json 查询网页 更新 y/n 生成网页并打开
    read_url(jason_filename)
    print("Over")
    h5.html_auto()


if __name__ == '__main__':
    main()
