#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 131_Palindrome_Partitioning.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp，构建一个二维dp表存储从i到j是否是回文，再进行dfs
    def partition(self, s):
        def dfs(s, res, dp, i, tmp):
            if i == len(s):
                res.append(tmp)
            for j in range(i, len(s)):
                if dp[i][j]:
                    dfs(s, res, dp, j + 1, tmp + [s[i: j + 1]])
            return
        
        l = len(s)
        dp = [[0] * l for i in range(l)]
        #构建dp表
        for j in range(l):
            dp[j][j] = 1
            for i in range(j):
                if i == j - 1:
                    if s[i] == s[j]: dp[i][j] = 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
        res = []
        dfs(s, res, dp, 0, [])
        return res


s = "aabbaa"
solute = Solution()
res = solute.partition(s)
