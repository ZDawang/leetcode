#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 72_Edit_Distance
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP, dp[i][j]代表word1的0-i 转为 word2的0-j所需要的最小步数
    #插入一个字母，删除一个字母，替代一个字母
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        if not word1: return l2
        if not word2: return l1
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        for i in range(l1 + 1):
            dp[i][0] = i
        for i in range(l2 + 1):
            dp[0][i] = i
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

word1 = "a"
word2 = "b"
solute = Solution()
res = solute.minDistance(word1, word2)

