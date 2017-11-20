#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 378_Kth_Smallest_Element_in_a_Sorted_Matrix.py
#time_complecity:  
#space_complecity: 
#beats: 
from heapq import *
class Solution(object):
    #堆，O(klogk)
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []
        #初始堆，将第一行都加入
        for i in range(min(k, n)):
            heap.append([matrix[0][i], 0, i])
        i = 0
        while i < k:
            minnum, row, col = heapq.heappop(heap)
            if row < n - 1:
                heapq.heappush(heap, [matrix[row + 1][col], row + 1, col])
        return minnum



