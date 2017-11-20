#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 685_Redundant_Connection_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #仍然是找环，但是需要去除环中的哪条边则不一定了。
    #只有两种异常情况：
    #第一种，有一个节点有两个父节点
    #第二种，跟684题一样，有一个环
    #对于第一种，找到这两个边，把后面一个边去掉，看能否找到环，找不到则说明是一颗正常的树，则去掉的边就是结果
    #若是能找到，则第一条边是结果
    #对于第二种，也是找环，若是能找到，则把当前边去掉
    def findRedundantDirectedConnection(self, edges):
        def find(x):
            if uf[x] != x: uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return False
            uf[x] = y
            return True
        #寻找有没有两个parent的节点
        parent = {}
        firstedge, secondedge = [], []
        for pa, ch in edges:
            if ch in parent:
                firstedge = [parent[ch], ch]
                secondedge = [pa, ch]
            else:
                parent[ch] = pa
        #去除第二个边
        if secondedge: edges.remove(secondedge)
        #找环
        uf = {}
        for pa, ch in edges:
            if not pa in uf: uf[pa] = pa
            if not ch in uf: uf[ch] = ch
            if not union(pa, ch):
                return firstedge or [pa, ch]
        return secondedge