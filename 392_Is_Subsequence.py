#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-5
#difficulty degree：
#problem: 392_Is_Subsequence
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isSubsequence(self, s, t):
        if not s: return True
        lt, ls = len(t), len(s)
        count = 0
        for i in range(lt):
            if t[i] == s[count]:
                if count == ls -1:
                    return True 
                count += 1
        return False

