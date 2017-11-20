#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-23
#difficulty degree：
#problem: 233_Number_of_Digit_One
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #按位挨个统计当前位的1的个数
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        res, ncopy, power = 0, n, 1
        while ncopy > 0:
            digit = ncopy % 10
            ncopy = ncopy // 10
            res += ncopy * power
            if digit == 1:
                res += 1 + n % power
            if digit > 1:
                res += power
            power *= 10
        return res




solute = Solution()
res = solute.countDigitOne(123)
print(res)