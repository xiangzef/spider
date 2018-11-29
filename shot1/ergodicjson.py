#！coding:utf-8
#导入json模块，你也可以用simplejson，一个第三模块，比较好用
import json

jsonpath = "Book.json"
#定义一个dict对象，并有些value还是以json的形式出现，形式如下
adict={"xiaoqiangk":"xiaoqiangv","xiaofeik":"xiaofeiv","xiaofeis":{"xiaofeifk":"xiaofeifv","xiaofeimk":{"xiaoqik":"xiaoqiv","xiaogou":{"xiaolei":"xiaolei"}}},"xiaoer":{"xiaoyuk":"xiaoyuv"}}
#定义一个函数，用来处理json，传入json1对象，层深初始为0，对其进行遍历
def hJson(jsonpath,i=0):

    with open("Book.json",encoding="UTF-8") as jsonres:
        json1 = json.loads(jsonres.read())
        if(isinstance(json1,dict)):
    #遍历json1对象里边的每个元素
            for item in json1:
        #如果item对应的value还是json对象，就调用这个函数进行递归，并且层深i加1，如果不是，直接z在else处进行打印
                if (isinstance(json1[item],dict)):
        #打印item和其对应的value
                    print("****"*i+"%s : %s"%(item,json1[item]))
        #调用函数进行递归，i加1
                    hJson(json1[item], i=i+1)
                else:
        #打印
                    print("****"*i+"%s : %s"%(item,json1[item]))
    #程序入口，对adict进行处理，第二个参数可以不传
        else:
            print("json1  is not josn object!")

def main():
    hJson(jsonpath,0)

if __name__ == '__main__':
    main()