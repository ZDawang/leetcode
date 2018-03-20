#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 73_set_matrix_zeroes
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def setZeroes(self, matrix):
        matrix_copy = [m[:] for m in matrix]
        d_row, d_col = [], []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix_copy[row][col] == 0:
                    if row in d_row:
                        for i in range(len(matrix)):
                            matrix[i][col] = 0
                        d_col.append(col)
                    else:
                        if col in d_col:
                            for j in range(len(matrix[0])):
                                matrix[row][j] = 0
                            d_row.append(row)
                        else:
                            for j in range(len(matrix[0])):
                                matrix[row][j] = 0
                            d_row.append(row)
                            for i in range(len(matrix)):
                                matrix[i][col] = 0
                            d_col.append(col)

    #使用第一行，第一列来记录当前行与列的清零情况，使用row0，col0记录第一行与第一列的清零情况
    def setZeroes2(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])

        row0, col0 = 1, 1
        for i in range(m):
            col0 &= (matrix[i][0] != 0)
        for j in range(n):
            row0 &= (matrix[0][j] != 0)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0
        if row0 == 0:
            for j in range(n):
                matrix[0][j] = 0
        

#matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
matrix = [[0]]
solute = Solution()
solute.setZeroes(matrix)

for m in matrix:
    print(m)