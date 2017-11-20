#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 516_Longest_Palindromic_Subsequence
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp[i][j]来记录i到j的最长子序列长度，进行迭代
    #TLE
    def longestPalindromeSubseq(self, s):
        l = len(s)
        dp = [[0]*l for i in range(l)]
        for i in range(l):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])
        return dp[0][-1]

    #dp重复使用，因为第10个字母时，用不到第8个字母的结果
    def longestPalindromeSubseq2(self, s):
        l = len(s)
        dp = [0] * l
        for i in range(l):
            dp[i] = 1
            pre = 0
            for j in range(i - 1, -1, -1):
                tmp = dp[j]
                if s[j] == s[i]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j + 1], dp[j])
                pre = tmp
        return dp[0]


s = "abcdeff"
solute = Solution()
res = solute.longestPalindromeSubseq2(s)