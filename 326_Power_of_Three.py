#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-25
#difficulty degree：
#problem: 326_Power_of_Three
#time_complecity:  
#space_complecity: 
#beats: 
import math
class Solution(object):
    # 对数，或者拿3的幂次方的最大数去除
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        temp = math.log10(n) / math.log10(3)
        print(temp)
        if temp.is_integer():
            return True
        return False

solute = Solution()
res = solute.isPowerOfThree(242)
print(res)