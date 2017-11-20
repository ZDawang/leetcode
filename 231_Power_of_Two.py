#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-23
#difficulty degree：
#problem: 231_Power_of_Two
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #正常思路
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        remain = n % 2
        while remain != 1 and n != 1:
            n = n // 2
            remain = n % 2
        return True if n == 1 else False

    #使用2的幂次为100000形式
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        return not n & (n - 1)