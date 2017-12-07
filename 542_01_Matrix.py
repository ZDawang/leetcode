#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 542_01_Matrix
#time_complecity:  
#space_complecity: 
#beats: 

import heapq
class Solution(object):
    #使用堆
    def updateMatrix(self, matrix):
        #检测坐标(x, y)周围是否有0
        def isNearZero(x, y):
            return (x > 0 and matrix[x-1][y] == 0) or (x < m - 1 and matrix[x+1][y] == 0) or (y > 0 and matrix[x][y-1] == 0) or (y < n - 1 and matrix[x][y+1] == 0)

        if not matrix or not matrix[0]: return matrix
        m, n = len(matrix), len(matrix[0])
        heap = []
        visit = set()
        #将周围有0的1所在的位置加入到堆中，并标记为已访问
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 1 and isNearZero(x, y):
                    visit.add((x, y))
                    heapq.heappush(heap, (1, x, y))
        #当堆不为空时
        while heap:
            #弹出距离最小的点的坐标与距离
            dis, x, y = heapq.heappop(heap)
            #将周围满足条件的点加入到堆中，并标记为已访问。
            #满足的条件为：未访问过且matrix[newx][newy] == 1
            for newx, newy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if newx < 0 or newx >= m or newy < 0 or newy >= n:
                    continue
                if (newx, newy) in visit or matrix[newx][newy] == 0:
                    continue
                matrix[newx][newy] = dis + 1
                visit.add((newx, newy))
                heapq.heappush(heap, (dis + 1, newx, newy))
        return matrix