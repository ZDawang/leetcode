#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 476_Number_Complement.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #找到最高位的1，然后把n变为最高位及最高位后面全是1，与~num进行与
    def findComplement(self, num):
        n = 2**31
        while(n & num != n):
            n = n >> 1
        n = (n << 1) - 1
        return ~num & n