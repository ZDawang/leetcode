#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 684_Redundant_Connection.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #并查集，当union失败时，说明形成环。
    def findRedundantConnection(self, edges):
        def find(x):
            if uf[x] != x: uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return False
            uf[x] = y
            return True

        uf = {}
        for p0, p1 in edges:
            if not p0 in uf: uf[p0] = p0
            if not p1 in uf: uf[p1] = p1
            if not union(p0, p1): return [p0, p1]
