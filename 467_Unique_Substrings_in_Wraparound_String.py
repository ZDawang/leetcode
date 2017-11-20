#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 467_Unique_Substrings_in_Wraparound_String
#time_complecity:  
#space_complecity: 
#beats: 

#结果记录以当前字母结束的最多可能即可。
class Solution(object):
    def findSubstringInWraproundString(self, p):
        if not p:
            return 0
        res = 0
        tmp = 1
        dp = [0] * 26
        dp[ord(p[0]) - 97] = 1
        for i in range(1, len(p)):
            Ascii = ord(p[i])
            index = Ascii - 97
            preAscii = ord(p[i - 1])
            if preAscii == 122:
                preAscii = 96
            if Ascii == preAscii + 1:
                tmp += 1
                dp[index] = max(tmp, dp[index])
            else:
                tmp = 1
                dp[index] = max(tmp, dp[index])
        res = sum(dp)
        return res

p = "a"
solute = Solution()
res = solute.findSubstringInWraproundString(p)
