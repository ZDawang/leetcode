#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-25
#difficulty degree：
#problem: 357_Count_Numbers_with_Unique_Digits
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #挨个计算2位长度的数字有多少，3位长度的。。。。
    def countNumbersWithUniqueDigits(self, n):
        if n == 0：
            return 1
        temp = 9
        cnt = 9
        res = 10
        n = min(n, 10)
        while n > 1:
            temp = cnt * temp
            cnt -= 1
            res = res + temp
            n -= 1
        return res

solute = Solution()
res = solute.countNumbersWithUniqueDigits(3)
print(res)