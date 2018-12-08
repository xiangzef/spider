import bs4
import json

bakpath = 'C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks'
path = '../file/result.json'
def writbak():
    #输入文件
    f = open(bakpath ,'r',encoding='UTF-8')
    #输出文件
    fw = open(r'book.json','w', encoding='UTF-8')
    #按行读出所有文本
    lines = f.readlines()
    num = -1
    for line in lines:
        str = '@SES/%i/' %num
        line = line.replace('@SES/1/',str)
        num = num + 1
        #写入文件
        fw.writelines(line)
    #关闭文件句柄
    f.close()
    fw.close()

# def readbak():
#     # 输出文件
#     # 按行读出所有文本
#     with open(r'Bookmarks.txt', encoding='UTF-8') as f:
#         all_lines = f.readlines()
#         for line in all_lines:
#             if line.strip().find('name'):



def readjson():
    global path
    with open("Book.json",encoding="UTF-8") as f:
        fjson = json.loads(f.read())
        fenal_json = fjson['roots']['bookmark_bar']['children'][0]
        result = [(item.get('name', 'NA'), item.get('url', 'NA')) for item in fenal_json['children']]
    # with open(path, "w", encoding="utf-8") as js:
    #     json.dump(result, js, ensure_ascii=False)
    return result

def readbak():
    writbak()
    readjson()

