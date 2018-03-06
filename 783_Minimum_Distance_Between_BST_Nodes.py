#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 783_Minimum_Distance_Between_BST_Nodes.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #中序遍历
    def minDiffInBST(self, root):
        stack = []
        preval, minDiff = float("inf"), float("inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            minDiff = min(minDiff, abs(root.val - preval))
            preval = root.val
            root = root.right
        return minDiff