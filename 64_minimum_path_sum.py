#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 64_minimum_path_sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if i > 0:
                    grid[i][j] = (min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]) if j else grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = grid[i][j - 1] + grid[i][j] if j else grid[i][j]
        return grid[-1][-1]

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solute = Solution()
res = solute.minPathSum(grid)
print(res)