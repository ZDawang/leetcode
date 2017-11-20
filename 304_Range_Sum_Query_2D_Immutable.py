#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 304_Range_Sum_Query_2D_Immutable
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP
    #使用sums存储从(0,0)到(i,j)范围内的矩阵的元素之和。
    #所以(row1, col1)到(row2, col2)范围内的元素之和可以根据画图简单的推导出来
    #在矩阵的左边与上面扩增一圈0，这样免去判断边界的问题。
    def __init__(self, matrix):
        if not matrix: 
            self.sums = []
            return
        m, n = len(matrix), len(matrix[0])
        self.sums = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.sums[i + 1][j + 1] = matrix[i][j] + self.sums[i + 1][j] + self.sums[i][j + 1] - self.sums[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        if not self.sums: return 0
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][col1]