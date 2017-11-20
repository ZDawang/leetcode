#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-18
#difficulty degree：
#problem: 205_Isomorphic_Strings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用d来记住替换的规则。
    def isIsomorphic(self, s, t):
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        ds, dt = {}, {}
        for i in range(ls):  
            if s[i] not in ds:
                ds[s[i]] = t[i]
            if t[i] not in dt:
                dt[t[i]] = s[i]
            if (s[i] in ds and ds[s[i]] != t[i]) or (t[i] in dt and dt[t[i]] != s[i]):
                return False
        return True

solute = Solution()
res = solute.isIsomorphic("ab", "aa")
print(res)