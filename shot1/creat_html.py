import json
import webbrowser
import re
#len(re.findall(r'^[\u4e00-\u9fa5]{0,}$', str(re1['name']).strip().encode("utf-8")))
# 命名生成的html
GEN_HTML = "test.html"
json_path ="../file/result.json"
chromePath = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'  # 例如我的：C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe
row_numbers = 80

# 打开文件，准备写入
def creat_html(from_json):
    cnlen = 0
    enlen = 0
    Online = '<body><meta charset="utf-8"><strong><font size="2">Online:-------------------------------'+'<br /></strong>\r\n</body><table border="1">'
    Offline = '<body><meta charset="utf-8"><strong><font size="2">Offline:-------------------------------'+'<br /></strong>\r\n</body><table border="1">'
    with open (from_json,"r",encoding="utf-8") as js:
        res = json.loads(js.read())
        i = 0
        row_num1 = 0
        row_num2 = 0
        for re1 in res['result']:
            if str(re1['y/n']).strip().encode("utf-8") == str("在线").encode("utf-8"):
                if row_num1 == 0:
                    Online = Online + '<tr>'
                if str(re1['name']).strip().find('milkyway')>0:
                    row_num1 += 1
                    Online = Online + '<td width=300><a href="'+re1['url']+'" target="_blank "> '+ re1['name']+'❤❤❤❤❤'+'</a></td>'
                else:
                    row_num1 += 1
                    Online = Online + '<td width=300><a href="' + re1['url'] + '" target="_blank "> ' + re1['name']+'</a></td>'
            if str(re1['y/n']).strip().encode("utf-8") == str("不在线").encode("utf-8") and str(re1['name']) != '大香蕉直播間_全球美女直播_大香蕉伊人網_大香蕉网_伊人在线大香蕉':
                if row_num2 == 0:
                    Offline = Offline + '<tr>'
                if str(re1['name']).strip().find('milkyway')>0:
                    row_num2 += 1
                    Offline = Offline + '<td width=300><a href="' + re1['url'] + '" target="_blank "> ' + re1['name'] + '❤❤❤❤❤'+'</a></td>'
                else:
                    row_num2 += 1
                    Offline = Offline + '<td width=300><a href="' + re1['url'] + '"target="_blank"> ' + re1['name'] +'</a></td>'
            if row_num1 == 2:
                row_num1 = 0
                Online = Online + '</tr>\r\n'
            if row_num2 == 2:
                row_num2 = 0
                Offline = Offline + '</tr>\r\n'
            i += 1
    return Online, Offline

def html_auto():
    f = open(GEN_HTML, 'w',encoding='utf-8')
    lst = creat_html(json_path)

    message = """
    <html>
    <head><meta charset="utf-8"></head>
    <body><meta charset="utf-8">
    <font size="1">%s</table>
    <font size="1">%s</table>
    </body>
    </html>""" % (lst[0], lst[1])
    f.write(message)
    # 关闭文件
    f.close()
    # 运行完自动在网页中显示
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    webbrowser.get('chrome').open_new_tab(GEN_HTML)

if __name__ == '__main__':
    main()
# 运行完自动在网页中显示
