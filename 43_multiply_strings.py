#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 43_multiply_strings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 =='0':
            return "0"
        res = [0] * (len(num1) + len(num2))
        index = len(num1) + len(num2)
        for n1 in reversed(num1):
            index = index - 1
            start = index
            for n2 in reversed(num2):
                res[start] += int(n1) * int(n2)
                res[start - 1] += res[start] // 10
                res[start] %= 10
                start -= 1
        return ''.join(map(str,res[0:])) if res[0] != 0 else ''.join(map(str,res[1:]))


num1 = "300"
num2 = "30"

solute = Solution()
res = solute.multiply(num1, num2)

print(res)