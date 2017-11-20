#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 543_Diameter_of_Binary_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def diameterOfBinaryTree(self, root):
        def dfs(root, res):
            if root == None: return -1
            l, r = dfs(root.left, res), dfs(root.right, res)
            res[0] = max(res[0], l + r + 2)
            return max(l + 1, r + 1)
        res = [0]
        dfs(root, res)
        return res[0]