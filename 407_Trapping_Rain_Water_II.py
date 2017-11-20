#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 407_Trapping_Rain_Water_II.py
#time_complecity:  
#space_complecity: 
#beats: 
from queue import PriorityQueue
class Solution(object):
    #从边沿向里，存储每个board的最小高度边界
    #heapq速度更快
    #每个board能存水量，是看它能四周的边界最低的那个，所以用堆来从低到高，找出所有board的最低边界
    #最低边界的意思是，不溢出这个沙盒的最高水位
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]: return 0s
        h, w = len(heightMap), len(heightMap[0])
        heap = PriorityQueue()
        visit = [[0] * w for _ in range(h)]
        res = 0
        #将边沿的高度加入堆中
        for i in (0, h - 1):
            for j in range(w):
                heap.put((heightMap[i][j], i, j))
                visit[i][j] = 1
        for j in (0, w - 1):
            for i in range(1, h-1):
                heap.put((heightMap[i][j], i, j))
                visit[i][j] = 1
        #
        while not heap.empty():
            height, i, j = heap.get()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < h and 0 <= y < w and not visit[x][y]:
                    res += max(0, height - heightMap[x][y])
                    heap.put((max(heightMap[x][y], height), x, y))
                    visit[x][y] = 1
        return res


    #BFS



