import requests
import json

def get_url(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    }
    res = requests.get(url,headers = headers)
    return res

def is_online(res)
    netjson = json.load(res.text)
    online_or_not = netjson['nowpage']
    with open('is_online.txt','w',encoding='utf-8') as file:
        for each in online_or_not:
            if 
            file.write(each[])



def main():
    url = 'http://www.du871.com/index-show-iNWlERWAJQA9nA75PKMx1HelbE8_3D.htm'
    res = get_url(url)


    print("Over")

if __name__ == '__main__':
    main()
