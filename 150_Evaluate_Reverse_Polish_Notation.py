#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10-18
#difficulty degree：
#problem: 150_Evaluate_Reverse_Polish_Notation.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    stack.append(-stack.pop() + stack.pop())
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    divisor = stack.pop()
                    divdend = stack.pop()
                    div = abs(divdend)/abs(divisor)
                    div = div if divisor * divdend >= 0 else -div
                    stack.append(div)
        return stack[-1]