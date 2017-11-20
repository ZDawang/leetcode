#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-12
#difficulty degree：
#problem: 200_Number_of_Islands
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #遍历一个岛上的所有点，然后将岛上的点全赋值为0，然后遍历下一个岛, 或者使用一个全局字典记录已遍历过的位置
    def numIslands(self, grid):
        def dfs(pos_x, pos_y, m, n):
            if pos_x < 0 or pos_x >= m or pos_y < 0 or pos_y >= n or grid[pos_x][pos_y] == "0":
                return
            if (pos_x, pos_y) in d: return
            d.add((pos_x, pos_y))
            dfs(pos_x + 1, pos_y, m, n)
            dfs(pos_x - 1, pos_y, m, n)
            dfs(pos_x, pos_y + 1, m, n)
            dfs(pos_x, pos_y - 1, m, n)
            return

        if not grid: return 0
        res = 0
        d = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if (i, j) in d:
                    continue
                res += 1
                dfs(i, j, m, n)
        return res

    #并查集,使用i*n+j来代表位置
    def numIslands2(self, grid):
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return False
            uf[x] = y
            return True

        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        #初始化并查集
        uf = [i for i in range(m * n)]
        count = sum([1 if grid[i][j] == "1" else 0 for i in range(m) for j in range(n)])
        #每个岛只需要跟上面还有左边的融合
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0": continue
                loc = i * n + j
                if i > 0 and grid[i - 1][j] == "1":
                    count -= union(p, p - n)
                if j > 0 and grid[i][j - 1] == "1":
                    count -= union(p, p - 1)
        return count



solute = Solution()
grid = [["1", "1", "1"],["0", "1", "0"],["1", "1", "1"]]
res = solute.numIslands(grid)



