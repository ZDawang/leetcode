#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 74_search_a_2d_matrix
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #二分法，将二维数组看成1维数组来对待
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        mid = (l + r)//2
        while(l <= r):
            mid = (l + r)//2
            if matrix[mid//n][mid%n] == target:
                return True
            if matrix[mid//n][mid%n] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

matrix = [[0]]
target = 0
solute = Solution()
res = solute.searchMatrix(matrix, target)
print(res)