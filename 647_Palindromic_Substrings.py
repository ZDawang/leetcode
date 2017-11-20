#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 647_Palindromic_Substrings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp思路，存储i到j是否有回文子串，最后统计dp数组中的所有回文子串个数
    #时间复杂度O(n2)，空间复杂度为可优化为O(n2)
    def countSubstrings(self, s):
        l = len(s)
        dp = [[0] * l for i in range(l)]
        for j in range(l):
            #长度为1的回文子串
            dp[j][j] = 1
            for i in range(j):
                #判断是否为长度为2的回文子串
                if i == j - 1:
                    if s[i] == s[j]: dp[i][j] = 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
        return sum([sum(p) for p in dp])


    #空间复杂度优化，O(n)
    def countSubstrings2(self, s):
        res = 0
        l = len(s)
        dp = [0] * l
        for j in range(l):
            dp[j] = 1
            for i in range(j):
                dp[i] = 1 if s[i] == s[j] and dp[i + 1] == 1 else 0
            res += sum(dp)
        return res



s = "aaa"
solute = Solution()
res = solute.countSubstrings(s)

