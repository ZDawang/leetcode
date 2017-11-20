#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-1
#difficulty degree：
#problem: 54_spiral_matrix
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        h, w = len(matrix), len(matrix[0])
        u, d, l, r = 0, h - 1, 0, w - 1
        res = []
        while(1):
            res += matrix[u][l : r + 1]
            u += 1
            if u > d:
                break
            for row in range(u, d + 1):
                res.append(matrix[row][r])
            r -= 1
            if r < l:
                break
            for col in range(r, l - 1, -1):
                res.append(matrix[d][col])
            d -= 1
            if u > d:
                break
            for row in range(d, u - 1, -1):
                res.append(matrix[row][l])
            l += 1
            if r < l:
                break
        return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

solute = Solution()
res = solute.spiralOrder(matrix)
print(res)