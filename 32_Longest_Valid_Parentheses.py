#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 32_Longest_Valid_Parentheses
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路，使用dp[i]来存储到i的最长数
    def longestValidParentheses(self, s):
        if not s: return 0
        l = len(s)
        dp = [0] * l
        for i in range(1, l):
            if s[i] == "(":
                continue
            if s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]] if dp[i - 1] > 0 else 0
        return max(dp)
    
s = "()(())"
solute = Solution()
res = solute.longestValidParentheses(s)


