#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 48_rotate_image
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        mat_temp = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(matrix[i][j])
            mat_temp.append(temp)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = mat_temp[n - 1 - j][i]

matrix = [[1]]
for i in range(1):
    print(matrix[i])
solute = Solution()
solute.rotate(matrix)

for i in range(1):
    print(matrix[i])