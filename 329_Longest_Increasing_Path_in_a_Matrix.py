#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 329_Longest_Increasing_Path_in_a_Matrix.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS+memo
    def longestIncreasingPath(self, matrix):
        def dfs(i, j, preval):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= preval:
                return 0
            if i * n + j in memo:
                return memo[i * n + j]
            u = dfs(i + 1, j, matrix[i][j])
            d = dfs(i - 1, j, matrix[i][j])
            l = dfs(i, j - 1, matrix[i][j])
            r = dfs(i, j + 1, matrix[i][j])
            res = max(u, d, l, r) + 1
            memo[i * n + j] = res
            return res

        if not matrix or not matrix[0]:
            return 0
        memo = {}
        m, n = len(matrix), len(matrix[0])
        return max(dfs(i, j, float("-inf")) for i in range(m) for j in range(n))
