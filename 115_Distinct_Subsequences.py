#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 115_Distinct_Subsequences
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp[i][j]代表s的前i个字母的子串为t的前j个字母的数量,O(n2)
    def numDistinct(self, s, t):
        ls, lt = len(s), len(t)
        dp = [[0] * (lt + 1) for i in range(ls + 1)]
        dp[0][0] = 1
        for i in range(1, ls + 1):
            dp[i][0] = 1
            for j in range(1, lt + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    #On space
    def numDistinct2(self, s, t):
        ls, lt = len(s), len(t)
        dp = [1] + [0] * lt
        for i in range(1, ls + 1):
            newdp = [1] + [0] * lt
            for j in range(1, lt + 1):
                if s[i - 1] == t[j - 1]:
                    newdp[j] = dp[j] + dp[j - 1]
                else:
                    newdp[j] = dp[j]
            dp = newdp
        return dp[-1]

s = "b"
t = "a"

