#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-6
#difficulty degree：
#problem: 62_unique_paths
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def uniquePaths2(self, m, n):
        def move(pos_x, pos_y, m, n, res):
            if pos_x == n and pos_y == m:
                res[0] += 1
                return
            if pos_x > n or pos_y > m:
                return
            move(pos_x + 1, pos_y, m, n, res)
            move(pos_x, pos_y + 1, m, n, res)

        pos_x, pos_y = 1, 1
        res = [0]
        move(pos_x, pos_y, m, n, res)
        return res[0]

    def uniquePaths(self, m, n):
        res = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[-1][-1]




m, n = 3, 3
solute = Solution()
res = solute.uniquePaths(m, n)
print(res)