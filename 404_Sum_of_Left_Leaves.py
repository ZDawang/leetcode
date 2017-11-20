#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 404_Sum_of_Left_Leaves
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(node, isleft):
            if not node: return 0
            if not node.left and not node.right and isleft:
                return node.val
            return dfs(node.left, 1) + dfs(node.right, 0)
        if not root: return 0
        return dfs(root, 0)