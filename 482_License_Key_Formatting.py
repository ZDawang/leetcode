#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        stack, res = [], ""
        for c in S.upper():
            if c == "-":
                continue
            stack.append(c)
        while stack:
            i = 0
            while i < K and stack:
                res = stack.pop() + res
                i += 1
            res = "-" + res
        return res[1:]
