#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 85_Maximal_Rectangle
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路, 仿造第84题，对每一行做一次操作
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            #更新heights
            for j in range(n):
                heights[j] = 0 if matrix[i][j] == "0" else heights[j] + 1
            res = max(res, self.maxArea(heights))
        return res
        
    def maxArea(self, heights):
        heights.append(0)
        stack, res = [-1], 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res

    #DP思路






        