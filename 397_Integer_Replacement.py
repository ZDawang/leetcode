#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 397_Integer_Replacement
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def integerReplacement(self, n):
        res = 0
        while(n > 1):
            if n % 2 == 0:
                n = n // 2
            else:
                if n & 3 == 3 and n != 3:
                    n = n + 1
                else:
                    n = n - 1
            res += 1
        return res

