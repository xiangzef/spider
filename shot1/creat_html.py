import json
import webbrowser

# 命名生成的html
GEN_HTML = "test.html"
json_path ="../file/result.json"

# 打开文件，准备写入
def creat_html(from_json):
    Online = 'Online:'+'<br />\r\n'
    Offline = 'Offline:'+'<br />\r\n'
    with open (from_json,"r",encoding="utf-8") as js:
        res = json.loads(js.read())
        i = 0
        for re in res['result']:
            # if str(res['result'][i]['y/n']).strip().encode("utf-8") == str("在线").encode("utf-8"):
            #     Online = Online + res['result'][i]['name']+'<br />'+'<br />'+res['result'][i]['url']+res['result'][i]['y/n']+'<br /><br />\r\n'
            # if str(res['result'][i]['y/n']).strip().encode("utf-8") == str("不在线").encode("utf-8"):
            #     Offline = Offline + res['result'][i]['name']+'<br />'+res['result'][i]['url']+res['result'][i]['y/n']+'<br /><br />\r\n'
            if str(res['result'][i]['y/n']).strip().encode("utf-8") == str("在线").encode("utf-8"):

                Online = Online + '<a href="'+res['result'][i]['url']+'" target="_blank "> '+ res['result'][i]['name']+'</a><br/><br/>\r\n'
            if str(res['result'][i]['y/n']).strip().encode("utf-8") == str("不在线").encode("utf-8"):
                Offline = Offline + '<a href="' + res['result'][i]['url'] + '"target="_blank"> ' + res['result'][i]['name'] + '</a><br/><br/>\r\n'
            i = 1 + i
    return Online, Offline

def html_auto():
    f = open(GEN_HTML, 'w',encoding='utf-8')
    lst = creat_html(json_path)

    message = """
    <html>
    <head></head>
    <body>
    <p>%s</p>
    <p>%s</p>
    </body>
    </html>""" % (lst[0], lst[1])
    f.write(message)
    # 关闭文件
    f.close()
    # 运行完自动在网页中显示
    webbrowser.open(GEN_HTML, new=1)

if __name__ == '__main__':
    main()
# 运行完自动在网页中显示
