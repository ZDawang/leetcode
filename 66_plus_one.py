#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 66_plus_one
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def plusOne(self, digits):
        digits = [0] + digits
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits if digits[0] else digits[1:]
            digits[i - 1] += digits[i] % 10
            digits[i] -= 10
        return digits if digits[0] else digits[1:]

digits = [0]

solute = Solution()
res = solute.plusOne(digits)

print(res)
