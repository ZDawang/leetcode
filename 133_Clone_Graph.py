#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-11
#difficulty degree：
#problem: 133_Clone_Graph
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def __init__(self):
        self.d = {}
    def cloneGraph(self, node):
        if not node: return node
        if node.label in self.d:
            return self.d[node.label]
        newnode = UndirectedGraphNode(node.label)
        self.d[node.label] = newnode
        for neinode in node.neighbors:
            newnode.neighbors.append(self.cloneGraph(neinode))
        return newnode

