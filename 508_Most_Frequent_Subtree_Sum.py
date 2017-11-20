#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 508_Most_Frequent_Subtree_Sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #先构建字典，再运算
    def findFrequentTreeSum(self, root):
        def dfs(root, d):
            if not root: return 0
            tmp = dfs(root.left, d) + dfs(root.right, d) + root.val
            d[tmp] = d.get(tmp, 0) + 1
            return tmp
        d = {}
        dfs(root, d)

        maxtime = 0
        res = []
        for key in d:
            if d[key] > maxtime:
                res = [key]
            if d[key] == maxtime:
                res.append(key)
            maxtime = max(maxtime, d[key])
        return res

