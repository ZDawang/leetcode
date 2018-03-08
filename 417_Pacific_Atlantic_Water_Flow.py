#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 417_Pacific_Atlantic_Water_Flow.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):  
    #DFS. 从边界节点出发，记录所有能够到达的节点。
    def pacificAtlantic(self, matrix):
        def dfs(i, j, preval, visit):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if (i, j) in visit or matrix[i][j] < preval:
                return
            visit.add((i, j))
            dfs(i - 1, j, matrix[i][j], visit)
            dfs(i + 1, j, matrix[i][j], visit)
            dfs(i, j - 1, matrix[i][j], visit)
            dfs(i, j + 1, matrix[i][j], visit)

        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        p_visit, a_visit = set(), set()
        for i in range(m):
            dfs(i, 0, float("-inf"), p_visit)
            dfs(i, n - 1, float("-inf"), a_visit)
        for j in range(n):
            dfs(0, j, float("-inf"), p_visit)
            dfs(m - 1, j, float("-inf"), a_visit)
        return [list(g) for g in p_visit & a_visit]
            

    #BFS
    def pacificAtlantic2(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        #队列与已访问
        p_queue = collections.deque()
        a_queue = collections.deque()
        p_visit, a_visit = set(), set()
        #初始化队列
        for i in range(m):
            p_queue.append([i, 0])
            a_queue.append([i, n - 1])
        for j in range(n):
            p_queue.append([0, j])
            a_queue.append([m - 1, j])
        #BFS
        while p_queue:
            x, y = p_queue.popleft()
            p_visit.add((x, y))
            for newx, newy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if newx < 0 or newy < 0 or newx >= m or newy >= n:
                    continue
                if (newx, newy) in p_visit or matrix[newx][newy] < matrix[x][y]:
                    continue
                p_queue.append([newx, newy])
        while a_queue:
            x, y = a_queue.popleft()
            a_visit.add((x, y))
            for newx, newy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if newx < 0 or newy < 0 or newx >= m or newy >= n:
                    continue
                if (newx, newy) in a_visit or matrix[newx][newy] < matrix[x][y]:
                    continue
                a_queue.append([newx, newy])
        return [list(g) for g in p_visit & a_visit]




solute = Solution()

matrix = [[10,10,10],[10,1,10],[10,10,10]]
res = solute.pacificAtlantic(matrix)