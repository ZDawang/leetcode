#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-30
#difficulty degree：
#problem: 592_Fraction_Addition_and_Subtraction
#time_complecity:  
#space_complecity: 
#beats: 
from fractions import Fraction
class Solution(object):
    #先将分子与分母都提出来
    def fractionAddition(self, expression):
        res = sum(map(Fraction, expression.replace('+', ' +').replace('-', ' -').split()))
        return str(res.numerator) + '/' + str(res.denominator)

expression = "-1/2+1/2+1/3"
solute = Solution()
res = solute.fractionAddition(expression)
print(res)
