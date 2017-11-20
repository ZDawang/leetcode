#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-
#difficulty degree：
#problem: 221_Maximal_Square
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp存储每个点的最大矩阵,当当前数是1时，选择，左、上、左上的最小值+1
    def maximalSquare(self, matrix):
        if not matrix: return 0
        l1, l2 = len(matrix), len(matrix[0])
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] == "0":
                    dp[i + 1][j + 1] == 0
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
        res = max([max(row) for row in dp])
        return res*res
