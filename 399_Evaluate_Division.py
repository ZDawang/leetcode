#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 399_Evaluate_Division.py
#time_complecity:  
#space_complecity: 
#beats: 
import collections
class Solution(object):
    #思路，
    def calcEquation(self, equations, values, queries):
        def dfs(graph, dividend, divisor, visited, res):
            if not dividend in graph: return 0
            if divisor in graph[dividend]:
                return res * graph[dividend][divisor]
            for div in graph[dividend]:
                if div in visited: continue
                visited.add(div)
                tmp = dfs(graph, div, divisor, visited, res * graph[dividend][div])
                if tmp != 0: return tmp
            return 0

        #构建图
        graph = collections.defaultdict(dict)
        for value, (dividend, divisor) in zip(values, equations):
            graph[divisor][dividend] = 1/value
            graph[dividend][divisor] = value
            graph[dividend][dividend] = 1.0
            graph[divisor][divisor] = 1.0

        res = []
        for query in queries:
            tmp = dfs(graph, query[0], query[1], set(), 1.0)
            res.append(tmp if tmp != 0 else -1.0)
        return res

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

solute = Solution()
res = solute.calcEquation(equations, values, queries)