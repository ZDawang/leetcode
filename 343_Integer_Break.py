#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-25
#difficulty degree：
#problem: 343_Integer_Break
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def integerBreak(self, n):
        producttemp = 1
        if n <= 3:
            return n - 1
        for i in range(2, 4):
            num = n // i
            last = n % i
            if i * last > i + last:
                producttemp = max(i ** num * last, producttemp)
            else:
                producttemp = max(i ** (num - 1) * (last + i), producttemp)
        return producttemp

    def integerBreak2(self, n):
        return ((n % 3 + 3 + (n%3 == 2))*3**(n/3-1)) if (n>3) else (n-1)

solute = Solution()
res = solute.integerBreak(3)
print(res)