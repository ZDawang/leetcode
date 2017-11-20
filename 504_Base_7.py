#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def convertToBase7(self, num):
        if num == 0: return "0"
        sign = 1 if num >= 0 else -1
        num = abs(num)
        res = ""
        while num > 0:
            num, remain = divmod(num, 7)
            res = str(remain) + res
        return res if sign == 1 else "-" + res