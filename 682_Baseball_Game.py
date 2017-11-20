#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #是数字时直接入栈，是其它的时候分别进行处理。
    #因为有负号，所以没法用isdigit()方法，直接try看是否是数字。
    def calPoints(self, ops):
        score = []
        for op in ops:
            try:
                score.append(int(op))
            except:
                if op == "+":
                    score.append(score[-1] + score[-2])
                elif op == "D":
                    score.append(2 * score[-1])
                else:
                    score.pop()
        return sum(score)