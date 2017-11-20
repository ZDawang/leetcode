#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-26
#difficulty degree：
#problem: 227_Basic_Calculator_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def calculate(self, s):
        num, stack = 0, []
        operate = {"+", "-", "*", "/"}
        l = len(s)
        sign = "+"
        for i in range(l):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in operate or i == l - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    tmp = stack.pop()
                    if tmp < 0:
                        stack.append(-(-tmp // num))
                    else:
                        stack.append(tmp // num)
                num, sign = 0, s[i]
        return sum(stack)

s = "1"
solute = Solution()
res = solute.calculate(s)