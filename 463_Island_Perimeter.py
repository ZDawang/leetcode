#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 463_Island_Perimeter
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #将grid周围加一圈0，再计算
    def islandPerimeter(self, grid):
        h, w = len(grid), len(grid[0])
        newgrid = [[0] * (w + 2)]
        for g in grid:
            newgrid.append([0] + g + [0])
        newgrid.append([0] * (w + 2))
        res = 0
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                if newgrid[i][j]:
                    res += 4 - newgrid[i - 1][j] - newgrid[i + 1][j] - newgrid[i][j - 1] - newgrid[i][j + 1]
        return res

    def islandPerimeter2(self, grid):
        if not grid: return 0
        h, w = len(grid), len(grid[0])
        res = 0
        for i in range(h):
            for j in range(w):
                #若不是小岛，则contine
                if not grid[i][j]: continue
                #分别检查上下左右是否有边界，可以加入周长。
                u = i == 0 or grid[i - 1][j] == 0
                d = i == h - 1 or grid[i + 1][j] == 0
                l = j == 0 or grid[i][j - 1] == 0
                r = j == w - 1 or grid[i][j + 1] == 0
                res += u + d + l + r
        return res


solute = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
res = solute.islandPerimeter2(grid)
print(res)  
