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

#matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
matrix = [[0]]
solute = Solution()
solute.setZeroes(matrix)

for m in matrix:
    print(m)