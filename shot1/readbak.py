import bs4
import json
def writbak():
    #输入文件
    f = open(r'Bookmarks.bak' ,encoding='UTF-8')
    #输出文件
    fw = open(r'Bookmarks.txt','w', encoding='UTF-8')
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
    with open("Book.json",encoding="UTF-8") as f:
        fjson = json.loads(f.read())
        fenal_json = fjson['roots']['bookmark_bar']['children'][0]
        result = [(item.get('name', 'NA'), item.get('url', 'NA')) for item in fenal_json['children']]
    return result

def main():
    readjson()

if __name__ == '__main__':
    main()