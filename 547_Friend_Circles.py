#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 547_Friend_Circles.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #并查集，或者dfs+visited
    def findCircleNum(self, M):
        def find(x):
            if uf[x] != x: uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return False
            uf[x] = y
            return True

        n = len(M)
        count, uf = n, [i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if M[i][j] == 0: continue
                count -= union(i, j)
        return count

