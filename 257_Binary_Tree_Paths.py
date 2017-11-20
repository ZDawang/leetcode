#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 257_Binary_Tree_Paths
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(node, path):
            if node == None: return []
            newpath = path + "->" + str(node.val)
            if not node.left and not node.right:
                return [newpath]
            return dfs(node.left, newpath) + dfs(node.right, newpath)
        if not root: return []
        path = str(root.val)
        if not root.left and not root.right: return [path]
        return dfs(root.left, path) + dfs(root.right, path)