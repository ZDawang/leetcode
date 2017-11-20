#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 29_divide_two_integers
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #将被除数用除数乘2的幂次的累加表示。
    def divide(self, dividend, divisor):
        index = 1
        res = 0
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        remainder = abs_dividend
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            index = -1
        if abs_dividend == abs_divisor:
            return 1 if index == 1 else -1
        while(abs_divisor <= remainder):
            power_divisor = abs_divisor
            res_add = 1
            while(power_divisor < remainder):
                power_divisor_half = power_divisor
                res_add_half = res_add
                power_divisor = power_divisor + power_divisor
                res_add = res_add + res_add
            remainder = remainder - power_divisor_half
            res = res + res_add_half
        if index == -1:
            if remainder == 0:
                res = res - res - res
            else:
#此处有疑问，leetcode上默认-2/5 = 0 而不是-1
                res = res - res - res
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res

dividend = -2147483648
divisor = 1

solute = Solution()
res = solute.divide(dividend, divisor)

print(res)
