#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 310_Minimum_Height_Trees.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import defaultdict
class Solution(object):
    #第一思路：DFS
    #可以认为，只与其它一个节点有连接的是叶节点。
    #一个节点的深度，是它到所有叶节点的最大距离，所以可以从所有叶节点开始DFS，不断更新所有节点的深度。
    #DFS时间复杂度为O(叶节点数目*N)，时间复杂度太高，所以使用BFS
    #所以从所有叶节点进行BFS，如果一个节点只剩一个方向没有遍历，则把它加入下一层。
    #这样，最后一层，则是深度最小的节点。
    #时间复杂度为O(N)
    def findMinHeightTrees(self, n, edges):
        #构建图字典,e是边
        neighbor = defaultdict(list)
        neighbornum = defaultdict(int)
        for n1, n2 in edges:
            neighbor[n1].append(n2)
            neighbor[n2].append(n1)
            neighbornum[n1] += 1
            neighbornum[n2] += 1
        #检查是否存在没有边的单节点
        if len(neighbor) < n:
            return [node for node in range(n) if neighbornum[node] == 0]
        #将叶节点加入
        curlevel = [node for node in neighbor if neighbornum[node] == 1]
        visit = set()
        while True:
            nextlevel = []
            for curnode in curlevel:
                visit.add(curnode)
                for nextnode in neighbor[curnode]:
                    if nextnode in visit:
                        continue
                    neighbornum[nextnode] -= 1
                    #将只有一个方向的节点加入到下一层中
                    if neighbornum[nextnode] == 1:
                        nextlevel.append(nextnode)
            if not nextlevel:
                return curlevel
            curlevel = nextlevel



n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
solute = Solution()
res = solute.findMinHeightTrees(n, edges)



