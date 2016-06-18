#!/usr/bin/env python
#coding:utf-8
"""
__title__ = ''
__author__ = 'hadoop'
__mtime__ = '2016/6/18'
"""


import os
from time import clock as now

def list_dir(rootDir):
    fileNum=0
    deleteNum =0
    str = r'副本'  # 删除文件名中含有）的文件
    dirs = []
    dirs.append(rootDir)
    for root in dirs:
        for lists in os.listdir(root):
            path=os.path.join(root,lists)
            if os.path.isdir(path):
                dirs.append(path)
            else:
                fileNum += 1
                filename = os.path.basename(path)
                print filename.decode('gbk')
                if str in filename.decode('gbk'):
                    deleteNum += 1
                    print '删除文件：',path.decode('gbk')
                    os.remove(path)

    print '文件总个数为：', fileNum
    print '删除文件总个数为：',deleteNum




if __name__=='__main__':
    rootDir = raw_input("输入需要处理文件的根目录：")
    start=now()
    list_dir(rootDir)
    end=now()
    print ' 总共耗时：',end-start,'秒'
