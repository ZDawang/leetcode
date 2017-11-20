#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 28_implement_str
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def strStr(self, haystack, needle):
        len_needle = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1

haystack = "hglhsldkgdsf"
needle = "dagg"
solute = Solution()

res = solute.strStr(haystack, needle)
print(res)
