#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 695_Max_Area_of_Island.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS,把遍历过的小岛都变为0
    def maxAreaOfIsland(self, grid):
        def dfs(grid, x, y):
            #出界或者不是小岛
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            #将dfs过的小岛置为0
            grid[x][y] = 0
            return dfs(grid, x - 1, y) + dfs(grid, x + 1, y) + dfs(grid, x, y - 1) + dfs(grid, x, y + 1) + 1

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    res = max(res, dfs(grid, x, y))
        return res