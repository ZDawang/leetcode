#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 797_All_Paths_From_Source_to_Target.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS
    def allPathsSourceTarget(self, graph):
        def dfs(i, tmp):
            if i == n-1:
                res.append(tmp)
                return
            for j in graph[i]:
                dfs(j, tmp + [j])
        res, n = [], len(graph)
        dfs(0, [0])
        return res