#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 332_Reconstruct_Itinerary.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import defaultdict
class Solution(object):
    #典型DFS, 使用memo记录剩余的机票
    def findItinerary(self, tickets):
        def dfs(start):
            if len(trip) == dfs.length:
                return True
            for end in d[start]:
                if memo[start + end] <= 0:
                    continue
                memo[start + end] -= 1
                trip.append(end)
                if dfs(end):
                    return True
                trip.pop()
                memo[start + end] += 1
            return False

        #构建字典作为图
        d = defaultdict(list)
        memo = defaultdict(int)
        for (start, end) in tickets:
            d[start].append(end)
            memo[start + end] += 1
        #将d进行排序，使出发地字母小的先遍历
        for start in d:
            d[start].sort()
        trip = ["JFK"]
        dfs.length = len(tickets) + 1
        dfs("JFK")
        return trip