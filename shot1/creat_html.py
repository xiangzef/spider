import json
import webbrowser

# 命名生成的html
GEN_HTML = "test.html"
json_path ="../file/result.json"
chromePath = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'  # 例如我的：C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe


# 打开文件，准备写入
def creat_html(from_json):
    Online = '<body><meta charset="utf-8"><strong><font size="4">Online:-------------------------------'+'<br /></strong>\r\n</body>'
    Offline = '<body><meta charset="utf-8"><strong><font size="4">Offline:-------------------------------'+'<br /></strong>\r\n</body>'
    with open (from_json,"r",encoding="utf-8") as js:
        res = json.loads(js.read())
        i = 0
        for re in res['result']:
            if str(res['result'][i]['y/n']).strip().encode("utf-8") == str("在线").encode("utf-8"):
                if str(re['name']).strip().find('milkyway')>0:
                    Online = Online + '<a href="'+res['result'][i]['url']+'" target="_blank "> '+ res['result'][i]['name']+'❤❤❤❤❤'+'</a><br/><br/>\r\n'
                else:
                    Online = Online + '<a href="' + res['result'][i]['url'] + '" target="_blank "> ' + res['result'][i]['name'] + '</a><br/><br/>\r\n'
            if str(res['result'][i]['y/n']).strip().encode("utf-8") == str("不在线").encode("utf-8"):
                if str(re['name']).strip().find('milkyway')>0:
                    Offline = Offline + '<a href="' + res['result'][i]['url'] + '" target="_blank "> ' + res['result'][i]['name'] + '❤❤❤❤❤' + '</a><br/><br/>\r\n'
                else:
                    Offline = Offline + '<a href="' + res['result'][i]['url'] + '"target="_blank"> ' + res['result'][i]['name'] + '</a><br/><br/>\r\n'
            i = 1 + i
    return Online, Offline

def html_auto():
    f = open(GEN_HTML, 'w',encoding='utf-8')
    lst = creat_html(json_path)

    message = """
    <html>
    <head><meta charset="utf-8"></head>
    <body><meta charset="utf-8">
    <p><font size="3">%s</p>
    <p><font size="4">%s</p>
    </body>
    </html>""" % (lst[0], lst[1])
    f.write(message)
    # 关闭文件
    f.close()
    # 运行完自动在网页中显示
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    webbrowser.get('chrome').open_new_tab(GEN_HTML)
    # webbrowser.open(GEN_HTML, new=1)

if __name__ == '__main__':
    main()
# 运行完自动在网页中显示
