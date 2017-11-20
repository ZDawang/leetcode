#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 401_Binary_Watch.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #穷举
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]

    #排列组合
    def readBinaryWatch2(self, num):
        