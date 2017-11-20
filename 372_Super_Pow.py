#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 372_Super_Pow
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def superPow(self, a, b):
        a = a % 1337
        res = 1
        for num in b[::-1]:
            res *= a**num
            res %= 1337
            a = a**10 % 1337
        return res

solute = Solution()
a = 2147483647
b = [2,0,0]
res = solute.superPow(a, b)
print(res)