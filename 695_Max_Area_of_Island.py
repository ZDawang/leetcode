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

    #并查集
    #思路：如果当前数为1，跟上面、左边为1的并
    #并查集变化了一下，若是根节点，则uf[x]为负数，表示当前集合中元素个数，
    #若不是根节点，则uf[x]指向根节点。
    def maxAreaOfIsland2(self, grid):
        def find(x):
            if uf[x] < 0:
                return x
            uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return
            if uf[x] < uf[y]:
                uf[x], uf[y] = uf[x] + uf[y], x
            else:
                uf[y], uf[x] = uf[x] + uf[y], y

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        uf = [-1] * (m*n)
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                if i > 0 and grid[i - 1][j]:
                    union(i*n + j, (i-1)*n + j)
                if j > 0 and grid[i][j - 1]:
                    union(i*n + j, i*n + j - 1)
        return max([-uf[i*n + j] for i in range(m) for i in range(n) if grid[i][j]] or [0])

grid = [[0]]
solute = Solution()
res = solute.maxAreaOfIsland2(grid)