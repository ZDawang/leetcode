#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-6
#difficulty degree：
#problem: 63_unique_paths_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE  DFS
    def uniquePathsWithObstacles2(self, obstacleGrid):
        def move(pos_x, pos_y, m, n, obstacleGrid, res):
            if pos_x > n or pos_y > m:
                return
            if obstacleGrid[pos_y - 1][pos_x - 1]:
                return
            if pos_x == n and pos_y == m:
                res[0] += 1
                return
            move(pos_x + 1, pos_y, m, n, obstacleGrid, res)
            move(pos_x, pos_y + 1, m, n, obstacleGrid, res)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        pos_x, pos_y = 1, 1
        res = [0]
        move(pos_x, pos_y, m, n, obstacleGrid, res)
        return res[0]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[1 for i in range(n)] for j in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j]:
                    res[i][j] = 0
                elif i > 0:
                    res[i][j] = res[i - 1][j] + res[i][j - 1] if j else res[i - 1][j]
                else:
                    res[i][j] = res[i][j - 1] if j else res[i][j]
        return res[-1][-1]


#obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,0],[0,0],[0,1]]

solute = Solution()
res = solute.uniquePathsWithObstacles(obstacleGrid)
print(res)