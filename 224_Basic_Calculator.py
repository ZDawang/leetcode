#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-23
#difficulty degree：
#problem: 224_Basic_Calculator
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #如果碰到（，把当前结果与括号前符合存起来，不然就更新符号与结果
    def calculate(self, s):
        l = len(s)
        stack = []
        num = 0
        sign = 0  # +:0, -:1
        i = 0
        while i < l:
            if s[i] == " ":
                i += 1
                continue
            if s[i] == "(":
                stack.append(num)
                stack.append(sign)
                num = 0
                sign = 0
            elif s[i] == "-":
                sign = 1
            elif s[i] == "+":
                sign = 0
            elif s[i] == ")":
                sign_pop = stack.pop()
                num_pop = stack.pop()
                num = num + num_pop if sign_pop == 0 else num_pop - num
            else:
                digit = int(s[i])
                while i + 1 < l and s[i + 1].isdigit():
                    digit = digit * 10 + int(s[i + 1])
                    i += 1
                num = num + digit if sign == 0 else num - digit
            i += 1
        return num

s = " 2-1 + 2 "
solute = Solution()
res = solute.calculate(s)
print(res)

