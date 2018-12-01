
import json


# 自定义对象
class C(dict):
    name =str
    url =str
    y_n =str
    def __init__(self ,name ,url ,y_n ):
        self.name =name
        self.url =url
        self.y_n =y_n

class D(dict):
    result = dict
    def add_ele(self,result):
        self.result = self.result.update(result)
# 实例化自定义类
c1= C("天秀",  "http://www.du871.com/index-show-_2FjVQz_2BLfLzGrOYIK70KldA_3D_3D.htm","在线")
c2= C("天秀",  "http://www.du871.com/index-show-_2FjVQz_2BLfLzGrOYIK70KldA_3D_3D.htm","在线")
# json.dumps方法不能对自定义对象直接序列化,首先把自定义对象转换成字典

# overdict = c1.__dict__
# d1 = D()
# d1.result=[]
# print(c1)
# d1.add_ele(c1)
#
# # 此时就可以用json.dumps序列化了
# result = json.dumps(overdict, ensure_ascii=False)
# print(d1)
# print(type(d1))



