#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 766_Toeplitz_Matrix.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #将每一行的除了第一个，与前一行的除了第一个元素进行比较
    def isToeplitzMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return True
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if not (matrix[i][j] == matrix[i - 1][j - 1]):
                    return False
        return True

