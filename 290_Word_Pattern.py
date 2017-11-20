#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-18
#difficulty degree：
#problem: 290_Word_Pattern
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def wordPattern(self, pattern, str):
        s = str.split(" ")
        ls, lt = len(s), len(pattern)
        if ls != lt:
            return False
        ds, dt = {}, {}
        for i in range(ls):  
            if s[i] not in ds:
                ds[s[i]] = pattern[i]
            if pattern[i] not in dt:
                dt[pattern[i]] = s[i]
            if ds[s[i]] != pattern[i] or dt[pattern[i]] != s[i]:
                return False
        return True

pattern = "abba"
str1 = "dog cat cat dop"
solute = Solution()
res = solute.wordPattern(pattern, str1)
print(res)