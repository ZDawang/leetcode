#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 166_Fraction_to_Recurring_Decimal
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        flag = 0
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            flag = 1
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer = numerator // denominator
        remainder = numerator % denominator
        d = {}
        if remainder == 0:
            return "-" + str(integer) if flag else str(integer)
        decimal = ""
        i = 0
        while remainder not in d and remainder != 0:
            d[remainder] = i
            remainder *= 10
            decimal += str(remainder // denominator)
            remainder = remainder % denominator
            i += 1
        if remainder == 0:
            return "-" + str(integer) + '.' + decimal if flag else str(integer) + '.' + decimal
        temp = str(remainder * 10 // denominator)

        i = d[remainder]
        decimal = decimal[:i] + "(" + decimal[i:] + ")"
        return "-" + str(integer) + '.' + decimal if flag else str(integer) + '.' + decimal


numerator = 1
denominator = 6
solute = Solution()
res = solute.fractionToDecimal(numerator, denominator)
print(res)

