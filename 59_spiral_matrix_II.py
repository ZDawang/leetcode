#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-5
#difficulty degree：
#problem: 59_spiral_matrix_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def generateMatrix(self, n):
        u, d, l, r = 0, n - 1, 0, n - 1
        i = 1
        res = [[1 for j in range(n)] for j in range(n)]
        while(1):
            for col in range(l, r + 1):
                res[u][col], i = i, i + 1
            u += 1
            if u > d:
                break
            for row in range(u, d + 1):
                res[row][r], i = i, i + 1
            r -= 1
            if r < l:
                break
            for col in range(r, l - 1, -1):
                res[d][col], i = i, i + 1
            d -= 1
            if u > d:
                break
            for row in range(d, u - 1, -1):
                res[row][l], i = i, i + 1
            l += 1
            if r < l:
                break
        return res

solute = Solution()
res = solute.generateMatrix(3)
print(res)