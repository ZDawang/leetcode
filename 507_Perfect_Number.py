#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 507_Perfect_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        maxdiv = int(num**0.5)
        res = 0
        for i in range(1, maxdiv + 1):
            if num%i == 0:
                res += i + num//i
        return res == 2 * num