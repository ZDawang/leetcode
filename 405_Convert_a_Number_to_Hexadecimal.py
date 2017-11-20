#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 405_Convert_a_Number_to_Hexadecimal.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #直接位运算
    def toHex(self, num):
        if num == 0: return "0"
        d = "0123456789abcdef"
        res = ""
        for i in range(8):
            res = d[num & 15] + res
            num = num >> 4
        return res.lstrip("0")
