#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 17:04
# @Author  : ShenFeng
# @Site    : 
# @File    : calljar.py
# @Software: PyCharm


import os
import jpype
from jpype import *


# DES解密函数
def getpassword(data, firstkey, secondkey, thirdkey):
    """
    1. 使用.class调用

    """
    # 获得默认jvm路径，即jvm.dll文件路径
    # MacOS系统下执行后结果：/Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk/Contents/Home/jre/lib/jli/libjli.dylib
    jvmPath = jpype.getDefaultJVMPath()

    # util文件目录
    utilPath = os.path.abspath(os.path.dirname(__file__))

    # print utilPath

    # java扩展包路径，注意：这里的ext_classpath指的是.class文件的的引用路径之前的路径，如：
    # Javatest.class文件的全路径是：D:\code\H5\run\demo\src\com\Javatest.class，
    # Javatest类的包路径是com，所以此处ext_classpath='D:\code\H5\run\demo\src'；
    # JClass的路径就是Javatest类的包路径：JClass('com.Javatest')
    # 字符串前加r防止转译
    ext_classpath = utilPath + r'/jar'
    jvmArg = '-Djava.class.path=%s' % ext_classpath

    # print ext_classpath
    # print jvmArg

    if not jpype.isJVMStarted():
        # 启动Java虚拟机
        jpype.startJVM(jvmPath, '-ea', jvmArg)

    # 获取相应的Java类，并且创建类的实例
    javaClass = JClass("Des")
    javaInstance = javaClass()

    # 调用Java方法
    passwd = javaInstance.strDec(data, firstkey, secondkey, thirdkey)
    # 关闭jvm
    jpype.shutdownJVM()

    return passwd

# data = '96C00C8DD20C6EAA1A3C809F94F6ED84'
# first_key = 'chuangdada'
# second_key = '20180309'
# third_key = '13:27:57'
# # 结果为：admin123
# print getpassword(data, first_key, second_key, third_key)



"""
2. 使用.jar调用

"""
# startJVM(jvmPath, "-ea","-Djava.class.path=jar包的路径")
# JDClass = JClass("Des")
# jd = JDClass()
# print jd.strDec('96C00C8DD20C6EAA1A3C809F94F6ED84', 'chuangdada', '20180309', '13:27:57')
# shutdownJVM()
