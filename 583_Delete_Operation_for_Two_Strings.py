#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-27
#difficulty degree：
#problem: 583_Delete_Operation_for_Two_Strings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路，DP, dp[i][j]代表word1的前i个字符到word2的第j个字符所需要的最少步数
    #
    def minDistance(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        for j in range(l2 + 1):
            dp[0][j] = j
        for i in range(1, l1 + 1):
            dp[i][0] = i
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[-1][-1]

word1 = "sea"
word2 = "eat"
solute = Solution()
res = solute.minDistance(word1, word2)
