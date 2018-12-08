import threading
import json
import numpy
import spider_mate
import re

mutex_lock = threading.RLock()  # 互斥锁的声明
threads = []#存放线程的数组，相当于线程池


def read_url(path):
    global rate
    with open(path, encoding="utf-8") as js:
        result = json.loads(js.read())
        result_list = result['result']
        i = 0
        rate = round(len(result_list) / 7)
        lst = numpy.arange(1, len(result_list), 1)
        new_list = list(spider_mate.newlist(lst))
        for res in result_list:
            if i in new_list:
                print('{:.2%}'.format(i / len(result_list)), end='■')
            if i in numpy.arange(1, len(result_list), 3):
                print('', end='■')
            if res['y/n'] is not "错误链接":
                answer_name = spider_mate.ask(res['url'])
            res['y/n'] = answer_name[0]
            if str(answer_name[0]).strip() == '在线' and str(res['name']).strip() == '大香蕉直播間_全球美女直播_大香蕉伊人網_大香蕉网_伊人在线大香蕉' :
                result_list[i]['name'] = re.findall(r'[0-9a-zA-z_]+', str(answer_name[1]).strip().strip('\n'))[0]#正则表达式匹配大小写字母数字和下划线
            i = 1 + i
    with open(path, "w", encoding="utf-8") as js:
        json.dump(result, js, ensure_ascii=False)



class MyThread(threading.Thread):  # 线程处理函数
    def __init__(self , i, res, new_list,length):
        threading.Thread.__init__(self)  # 线程类必须的初始化
        self.i = i  # 将传递过来的name构造到类中的name
        self.res = res  # 将传递过来的name构造到类中的name
        self.new_list = new_list  # 将传递过来的name构造到类中的name
        self.length = length

    def run(self):
        # 声明在类中使用全局变量
        # 仅能有一个线程↓↓↓↓↓↓↓↓↓↓↓↓
        if self.res['y/n'] is not "错误链接":
            answer_name = spider_mate.ask(self.res['url'])
        self.res['y/n'] = answer_name[0]
        if str(answer_name[0]).strip() == '在线' and str(self.res['name']).strip() == '大香蕉直播間_全球美女直播_大香蕉伊人網_大香蕉网_伊人在线大香蕉' :
            self.res['name'] = re.findall(r'[0-9a-zA-z_]+', str(answer_name[1]).strip().strip('\n'))[0]#正则表达式匹配大小写字母数字和下划线
        # 仅能有一个线程↑↑↑↑↑↑↑↑↑↑↑↑
        mutex_lock.acquire()
        if self.i in self.new_list:
            print('{:.2%}'.format(self.i / self.length), end='■')
        if self.i in numpy.arange(1, self.length, 3):
            print('', end='■')
        mutex_lock.release()
    def result(self):
        try:
            return dict(self.res)  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def call_thr(i, res, new_list,length):
    thread = MyThread(i, res, new_list,length)#指定线程i的执行函数为myThread
    threads.append(thread)#先讲这个线程放到线程threads

def start_thr(result):
    for t in threads:#让线程池中的所有数组开始
        t.start()
    for t in threads:
        t.join()#等待所有线程运行完毕才执行一下的代码\
    i = 0
    for t in threads:
        result['result'][i] = t.res
        i += 1
