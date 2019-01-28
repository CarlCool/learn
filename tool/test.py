# -*- coding: utf-8 -*-
' a test module '
# for test use
# print("hello word")
# with open('C:/python/readme.txt', 'rb') as f:
#     print(f.read())
# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# s = f.read()
# print(s.strip())

# for i in range(5):
#     print(i)

# from multiprocessing import Process, Queue
# import os
# import time
# import random
# # 写数据进程执行的代码:
# def write(q):
#     """write q"""
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
    

# t = 0
#  s + s * r
# def total(y):
#     s = 150
#     r = 0.03
#     for i in range(y):
#         s = s + s * r
#     print(s);
# total(10);

# class A(object):
#     def __init__(self,a,b):
#         self.__a = a
#         self.__b = b

#     def myshow(self):
#         print('a=',self.__a,'b=',self.__b)

#     def __call__(self,num):
#         print('call:',num+self.__a+self.__b)
    
# a1=A(10,20)
# a1.myshow()

# a1(80)

# from collections import namedtuple
# Point = namedtuple('Poz', ['x', 'y', 'z'])
# p = Point(1,2,3)
# print(p.x)
# print(p.y)
# print(p.z)
# import struct
# s = struct.pack('>I', 1234)
# print(s)

# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

#     def end_element(self, name):
#         print('sax:end_element: %s' % name)

#     def char_data(self, text):
#         print('sax:char_data: %s' % text)

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)


# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# import requests
# r = requests.get('https://www.baidu.com')
# print(r.text)


# '''gui'''
# from tkinter import *
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()


# ''' remove the duplicate records'''
# import os
# BASE_DIR = os.path.abspath('.')
# # print(BASE_DIR)

# inputDir = os.path.join(BASE_DIR,'record.txt')
# outputDir = os.path.join(BASE_DIR,'result.txt')
# newList = []
# with open(inputDir, 'r') as f:
#     recordList = f.readlines()

# s = set(recordList)
# for i in s:
#     print("%s has found %s" % (i,recordList.count(i)))
# print(s)

# with open(outputDir, 'w') as fw:
#     fw.writelines(s)
# print('successfully')
# input()


# import asyncio

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# def a(s):
#     print("this is a")
#     print(s)
# def b():
#     print("this is b")
# a(b())


# def a():
#     print("start")
#     for i in range(5):
#         print("before:%s" %i)
#         x = yield i
#         print("after :%s" %i)
#         print("have sent %s" %x)
#     return None
# c = a()
# # for i in c:
# #     next(c)
# # x = next(c)
# # print("process:%s" %next(c))
# # print("this is %s"%len(c))
# # print("this is send part")
# # print("send: %s" %c.send(3))
# # print("send: %s" %c.send(4))
# def b():
#     w1 = yield from c
#     print("this is b() %s"%w1)
# d = b()
# try:
#     next(d)
#     d.send(9)
#     d.send(10)
#     d.send(11)
#     d.send(12)
#     d.send(13)
#     d.send(14)
# except:
#     print("exit")

# for j in d:
#     print("this is send part")
    # print("send %s" %c.send(j))

# list =["a","b","c"]
# for i,j in list:
#     print("%s:%s"%(i,j))


# def gen_one():
#     subgen = range(10)
#     print(subgen)
#     yield from subgen
# def gen_two():
#     subgen = range(10)    
#     for item in subgen:
#         print("item:%s"%item)
#         yield item
# def main():
#     a = gen_one()
#     print(next(a))
#     print(next(a))
#     print(next(a))
#     # print(next(gen_one()))
#     # print(next(gen_one()))
#     # print(next(gen_one()))
#     # print(next(gen_two()))
#     # print(next(gen_two()))
#     # print(next(gen_two()))
#     # print(next(gen_two()))
#     # print(next(gen_two()))
#     # print(next(gen_two()))
# main()

# def gen():
#     yield from subgen()
# def subgen():
#     while True:
#         x = yield
#         yield x+1
# def main():
#     g = gen()
#     next(g)                # 驱动生成器g开始执行到第一个 yield
#     retval = g.send(1)     # 看似向生成器 gen() 发送数据
#     print(retval)          # 返回2
#     # g.throw(StopIteration) # 看似向gen()抛入异常

# main()

# import aiohttp
# import asyncio
# # async with aiohttp.ClientSession() as session:
# # session = aiohttp.ClientSession()
# # resp = session.get('https://api.github.com/events')
# # print(resp.status)
# async def func():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.github.com/events') as resp:
#             print(resp.status)
#             print(await resp.text())

# # func()
# # next(a)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())
# loop.close() 
# lists=[1,2,3,4]
# assert len(lists) >=5,'列表元素个数小于5'

# assert 2==1
# print("here is the after")

# from aiohttp import web


# app = web.Application()
# web.run_app(app, host='127.0.0.1', port=8080)

# from aiohttp import web

# async def hello(request):
#     return web.Response(text="Hello, world")

# app = web.Application()
# app.router.add_get('/', hello)
# web.run_app(app)

# print("hello word")

# class A(object):
#     bar = 1
#     def func1(self):  
#         print ('foo') 
#     @classmethod
#     def func2(cls):
#         print ('func2')
#         print (cls.bar)
#         cls().func1()   # 调用 foo 方法

# a = A()
# a.func2()               # 不需要实例化

# import logging
# logging.warning("this is a waring")
# logging.error("this is error")
# print("end")

# x=lambda f: '`%s`' % f
# print(x("aadd1"))

# c=dict(a="b")
# print(c)
# attr={"a":"1s","b":"2s","d":"4s"}
# # attr["add"] = "3"
# kw=dict()
# for k,v in attr.items():
#     print(type(k))
#     print(k[0])
#     print(v[0])
#     kw[k]=v[1]
# print(attr)
# print(kw)

# list1 = []
# print(list1.__dir__())
# print(type(list1.__dir__))

# import asyncio 
# from aiohttp import ClientSession 
# async def fetch(url):      
#    async with ClientSession() as session:           
#       async with session.get(url) as response:
#           print(response)                     
#           return await response.read()
# loop = asyncio.get_event_loop() 
# # future = asyncio.ensure_future(fetch("https://www.baidu.com/"))
# loop.run_until_complete(fetch("https://www.baidu.com/"))

# def t(a,b):
#     return a,b
# print(t(1,2))
  
# url=URL(https://www.baidu.com)

# a = [1,2,3]
# b = [1,2,4]
# l = zip(a,b)
# for i in l:
#     print(i)
# # print(l)
# print("type : ",type(l))
# import os
# # path = os.path
# # path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# path = os.path.dirname(__file__)
# print(path)

# import re
 
# line = "Cats are smarter than dogs"
 
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")
# print ()

# import os
# import re
# BASE_DIR = os.path.abspath('.')
# # print(BASE_DIR)

# inputDir = os.path.join(BASE_DIR,'ttt.txt')
# outputDir = os.path.join(BASE_DIR,'result.txt')
# newList = []
# with open(inputDir, 'r') as f:
#     # fileList = f.readlines()
#     fileList = f.readlines()

# # for fl in fileList:
# #     # for n in fl:
# #     #     print(n)
# #     #     if(n="\t"):
# #     #         a = a + 1
# #     # print(a)
# #     newList.append(fl)
# # s = re.compile(r'(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s')
# s = re.compile(r'(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(.*)\s(\d+)\s(\d+)\s')
# # for x in newList:
# #     m = re.match(s,x)
# # x = newList[1]
# # m = re.match(s,x)
# # print(m.group(24))
# # s = r'[(.*)\s]{23}'
# for x in fileList:
#     # m = re.match(s,x)
#     if(s.match(x)):
#         print(s.match(x).group(24))
#     else:
#         print("miss")
#     # print(m.group(23))
# # print(newList)


# # with open(outputDir, 'w') as fw:
# #     fw.writelines(newList)
# # print('successfully')
# # input()

# import os
# from decimal import Decimal
# BASE_DIR = os.path.abspath('.')
# inputDir = os.path.join(BASE_DIR,'AIW_GENERAL_2017.txt')
# t1 = []
# t2 = []
# totalcost = 0
# totalrev = 0
# count = 0
# with open(inputDir, 'r') as f:
#     # t = tuple(f.readline().)
#     l = f.readline()
#     # recordlist = [i for i in l.split()]
#     # t = tuple(recordlist)
#     t = tuple([i for i in l.split()])
#     # print(t)
#     while True:
#         detailLine = f.readline()
#         if(not detailLine):
#             break
#         # t = t +tuple([i for i in detailLine.split()])
#         t = tuple([i for i in detailLine.split('\t')])
#         totalcost = totalcost + Decimal(t[23])
#         totalrev = totalrev + Decimal(t[22])
#         count = count + 1
#         # t1.append(t)
#     print('totalcost = ',totalcost)
#     print('totalrev = ',totalrev)
#     print('count = ',count)
    # wihle True:
    #     line = f.readline
# x = 1
# gen = (x for x in range(10))
# # gen.__next__
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())


str1 = 'ABCDEF'
if 'A' in str1:
    print('yes')
else:
    print('no')