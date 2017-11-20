#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-18
#difficulty degree：
#problem: 242_Valid_Anagram
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isAnagram(self, s, t):
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        ds, dt = {}, {}
        for i in range(ls):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
        return ds == dt