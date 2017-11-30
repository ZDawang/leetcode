#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 655_Print_Binary_Tree.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #先计算深度，然后再DFS
    #用d，i来标示node的位置
    def printTree(self, root):
        def getDepth(node):
            if not node: return 0
            return max(getDepth(node.left), getDepth(node.right)) + 1

        def dfs(node, d, i):
            if not node: return
            res[d][i] = str(node.val)
            tmp = 2**(dfs.depth - d - 2)
            dfs(node.left, d + 1, i - tmp)
            dfs(node.right, d + 1, i + tmp)

        dfs.depth = getDepth(root)
        res = [[""] * (2**dfs.depth - 1) for _ in range(dfs.depth)]
        dfs(root, 0, 2**(dfs.depth - 1) - 1)
        return res