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

import collections
    #BFS,没必要用堆，因为距离为1的后面肯定都是距离为2的，所以已经是有序的。
    #只用把堆换成队列就行了
    def updateMatrix2(self, matrix):
        def isNearZero(x, y):
            return (x > 0 and matrix[x-1][y] == 0) or (x < m - 1 and matrix[x+1][y] == 0) or (y > 0 and matrix[x][y-1] == 0) or (y < n - 1 and matrix[x][y+1] == 0)

        if not matrix or not matrix[0]: return matrix
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        visit = set()
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 1 and isNearZero(x, y):
                    visit.add((x, y))
                    queue.append((x, y))

        while queue:
            #弹出队首距离最小的点的坐标
            x, y = queue.popleft()
            dis = matrix[x][y]
            #将周围满足条件的点加入到堆中，并标记为已访问。
            #满足的条件为：未访问过且matrix[newx][newy] == 1
            for newx, newy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if newx < 0 or newx >= m or newy < 0 or newy >= n:
                    continue
                if (newx, newy) in visit or matrix[newx][newy] == 0:
                    continue
                matrix[newx][newy] = dis + 1
                visit.add((newx, newy))
                queue.append((newx, newy))
        return matrix

    #DFS
    #对于每个周围有0的点，都DFS一次，更新周围的1的距离
    #TLE
    def updateMatrix3(self, matrix):
        def isNearZero(x, y):
            return (x > 0 and matrix[x-1][y] == 0) or (x < m - 1 and matrix[x+1][y] == 0) or (y > 0 and matrix[x][y-1] == 0) or (y < n - 1 and matrix[x][y+1] == 0)

        def dfs(x, y, startx, starty, visit):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if (x, y) in visit or matrix[x][y] == 0:
                return
            #距离的计算。
            dis = abs(x - startx) + abs(y - starty) + 1
            if matrix[x][y] <= dis:
                return
            matrix[x][y] = dis
            visit.add((x, y))
            for newx, newy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                dfs(newx, newy, startx, starty, visit)

        if not matrix or not matrix[0]: return matrix
        m, n = len(matrix), len(matrix[0])
        #将为1的地方的值变为一个很大的值
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 1:
                    matrix[x][y] = m + n + 1
        #DFS
        for x in range(m):
            for y in range(n):
                if matrix[x][y] and isNearZero(x, y):
                    dfs(x, y, x, y, set())
        return matrix