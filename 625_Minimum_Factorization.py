#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-30
#difficulty degree：
#problem: 625_Minimum_Factorization
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def smallestFactorization(self, a):
        if a < 10: return a
        temp = []
        for i in range(9, 1, -1):
            while(a % i == 0):
                temp.append(str(i))
                a = a // i
        if a == 1:
            res = int("".join(temp[::-1]))
            if res < 2147483648 and res > -2147483643:
                return res
        return 0

solute = Solution()
