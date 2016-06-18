#!/usr/bin/env python
#coding:utf-8
"""
__title__ = ''
__author__ = 'hadoop'
__mtime__ = '2016/6/18'
"""

# 程序先运行，打印信息正确之后，取消os.remove(path)的注释，真正的删除文件

import os
from time import clock as now

def list_dir(rootDir):
    fileNum=0
    deleteNum =0
    sameName =0
    str = u'('  # 删除文件名中含有(的文件，这个可以根据实际需要改成想要的名字，现在是根据文件名识别，高级算法是根据图片内容找相似
    dirs = []
    files =[]   #保存文件名
    dirs.append(rootDir)
    for root in dirs:
        for lists in os.listdir(root):
            path=os.path.join(root,lists)
            if os.path.isdir(path):
                dirs.append(path)
            else:   #是文件
                fileNum += 1
                filename = os.path.basename(path)
                if filename.decode('gbk') in files:
                    sameName += 1
                    print '删除相同文件名的文件：',path.decode('gbk')
                else:
                    files.append(filename.decode('gbk'))
                    # os.remove(path)
                # print filename.decode('gbk')              #解码成gbk可以打印出中文名字，否则乱码
                # print(filename.decode('gbk').find(str))   #find返回的是找到字符串的位置,没找到返回-1
                if filename.decode('gbk').find(str)!= -1:
                    deleteNum += 1
                    print '删除文件：',path.decode('gbk')
                    # os.remove(path)
    print '文件总个数为：', fileNum
    print '删除重复文件总个数为：',deleteNum
    print '删除相同文件名总个数为：',sameName

if __name__=='__main__':
    rootDir = raw_input("输入需要处理文件的根目录：")
    start=now()
    list_dir(rootDir)
    end=now()
    print ' 总共耗时：',end-start,'秒'
