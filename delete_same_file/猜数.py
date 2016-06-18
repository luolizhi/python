#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'hadoop'
__mtime__ = '2016/6/18'
"""

#coding:utf-8
__author__ = 'Haddy Yang'

import random

class GuessNum():
    """猜数字类"""
    anwser = ''
    times = 0

    def __init__(self):
        pass

    def get_new(self):
    	#随机生成4位不重复数字
        self.anwser = ''.join(random.sample('0123456789', 4))
        self.times = 0
        return self.anwser

    def check_num(self, num):
        """检查数字
        	num :string ,4 number char
        """
        num = num[:4].ljust(4, ' ')
        self.times += 1
        a = b = 0
        for i, n in enumerate(num):
            if n == self.anwser[i]:
                a+=1
            elif n in self.anwser:
                b+=1

        return a, b

def main():
    print u'欢迎来猜数字 version:1.0 | 2016-05-24'
    guess = GuessNum()

    while True:
        guess.get_new()
        while True:
            num = raw_input(u'请输入4个数字：')
            a, b = guess.check_num(num)
            if a  == 4:
                print u'恭喜你猜到了！答案是%s，猜了%s次。' % (guess.anwser, guess.times)
                break
            else:
                print u'第%s次猜数字：%sA%sB' % (guess.times, a, b)

        is_continue = raw_input(u'是否还继续玩？(y/n)：'.encode('gbk')).lower()
        if is_continue != 'y':
            break

if __name__ == '__main__':
    main()