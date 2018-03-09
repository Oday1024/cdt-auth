#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 16:26
# @Author  : ShenFeng
# @Site    : 
# @File    : calljs.py
# @Software: PyCharm


import execjs


# 获取本地的js文件并返回js内容
def get_js():
    f = open("./js/md5.js", 'r')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# 读取js文件，并将js代码存入jsstr变量中
jsstr = get_js()

# print jsstr

# 执行编译js文件
ctx = execjs.compile(jsstr)

# 调用js中的方法，第一个参数是方法名，后面参数是改方法需要传入的参数
print(ctx.call('encryptMD5.strEnc', 'admin123', 'chuangdada', '20180309', '13:27:57'))