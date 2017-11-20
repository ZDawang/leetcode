#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 563_Binary_Tree_Tilt
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findTilt(self, root):
        def dfs(root, res):
            if not root: return 0
            l, r = dfs(root.left, res), dfs(root.right, res)
            res[0] += abs(l - r)
            return l + r + root.val
        res = [0]
        dfs(root, res)
        return res[0]