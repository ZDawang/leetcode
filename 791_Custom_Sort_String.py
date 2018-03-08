#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 791_Custom_Sort_String.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def customSortString(self, S, T):
        #统计S中各个字符的次序
        d = {}
        for i, c in enumerate(S):
            d[c] = i
        #排序
        return "".join(sorted(T, key = lambda x: d.get(x, 0)))