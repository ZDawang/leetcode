#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 363_Max_Sum_of_Rectangle_No_Larger_Than_K.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(n4)
    def maxSumSubmatrix(self, matrix, k):
        def maxSumSublist(vals):
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for val in vals:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum

        maxSum = float('-inf')
        columns = zip(*matrix)
        for left in range(len(columns)):
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                rowSums = map(int.__add__, rowSums, column)
                maxSum = max(maxSum, maxSumSublist(rowSums))
        return maxSum

matrix = [[2, 2,-1]]
solute = Solution()
res = solute.maxSumSubmatrix(matrix, 3)