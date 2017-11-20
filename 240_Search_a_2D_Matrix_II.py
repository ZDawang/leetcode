#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 240_Search_a_2D_Matrix_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #二分法，O(mlogn)
    def searchMatrix(self, matrix, target):
        def Binsearch(nums, target, length):
            l, r = 0, length - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return nums[l] == target

        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        row = m - 1
        while row > -1:
            if matrix[row][0] > target:
                row -= 1
            else:
                if Binsearch(matrix[row], target, n):
                    return True
                row -= 1
        return False

    #O(m + n)
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
