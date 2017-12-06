#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 144_Binary_Tree_Preorder_Traversal
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #递归
    def preorderTraversal(self, root):
        def dfs(node, res):
            res.append(node.val)
            if node.left: dfs(node.left, res)
            if node.right: dfs(node.right, res)
        if not root: return []
        res = []
        dfs(root, res)
        return res
    
    #迭代
    def preorderTraversal2(self, root):
        stack = []
        res = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    #迭代2
    def preorderTraversal3(self, root):
        if not root: return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right: stack.append(root.right)
            if root.left: stack.append(root.left)
        return res