#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 218_The_Skyline_Problem.py
#time_complecity:  
#space_complecity: 
#beats: 
from heapq import *
class Solution(object):
    #堆
    #总体思路是这样的，每次找到最小的x交点。
    #当一个新建筑与前面的最高建筑有重叠时，这时，看新建筑是否更高，若高则把左上角加入结果，否则不加
    #若与最高的没有重叠时，则最高的右边是最小的x交点。因为若有建筑右边小于最高建筑的右边，则会被包含进去。
    #需要注意的一点是，建筑物的左侧边界是递增的
    def getSkyline(self, buildings):
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []
        while i < n or liveHR:
            #当前建筑的左侧在最高建筑的右边，则最小的x交点是当前建筑的左侧
            if not liveHR or (i < n and buildings[i][0] <= -liveHR[0][1]):
                x = buildings[i][0]
                #防止重复把x点放入结果中。
                while i < n and buildings[i][0] == x:
                    heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                #最小的x交点是最高建筑的右侧，因为所有建筑的左侧都检查过了，其它右侧在最高建筑中的，肯定没有交点
                x = -liveHR[0][1]
                #把右侧在x前面的建筑全删掉。在上面删也行，把建筑左侧的建筑全删掉
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]

            #height != skyline[-1][1]是对于上面的判断来说的，
            if not skyline or height != skyline[-1][1]:
                skyline += [[x, height]]
            print(i, skyline)
        return skyline

    #简洁化
    def getSkyline2(self, buildings):
        scan = sorted([(L, -H, R) for L, R, H in buildings] + list((R, 0, None) for _, R, _ in buildings))
        heap, res = [(0, float("inf"))], [[0, 0]]
        for x, negH, R in scan:
            while x >= heap[0][1]: 
                heappop(heap)
            if negH: 
                heappush(heap, (negH, R))
            if -heap[0][0] != res[-1][1]:
                res.append([x, -heap[0][0]])
        return res[1:]








buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
solute = Solution()
res = solute.getSkyline(buildings)