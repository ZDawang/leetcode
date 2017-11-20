#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 132_Palindrome_Partitioning_II.py
#time_complecity:  
#space_complecity: 
#beats: 
import collections
class Solution(object):
    #DP+BFS,复杂度O(n2) 
    #TLE，原因应该是queue入栈出栈太费时了
    def minCut(self, s):
        #构建dp表
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
        #BFS
        queue = collections.deque()
        queue.append((0, 0))
        while queue:
            index, level = queue.popleft()
            if dp[index][l - 1]: return level
            for j in range(index, l - 1):
                if dp[index][j]:
                    queue.append((j + 1, level + 1))
        return 0

    def minCut2(self, s):
        #构建dp表
        l = len(s)
        dp = [[0] * l for i in range(l)]
        cut = [0] * l
        #构建dp表
        for j in range(l):
            minnum = j
            for i in range(j + 1):
                if s[i] == s[j] and (i + 1 > j - 1 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    minnum = 0 if i == 0 else min(minnum, cut[i - 1] + 1)
            cut[j] = minnum
        return cut[-1]


s = "aab"
solute = Solution()
res = solute.minCut2(s)