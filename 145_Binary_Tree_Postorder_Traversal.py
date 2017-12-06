#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 145_Binary_Tree_Postorder_Traversal
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #递归写法
    def postorderTraversal(self, root):
        def dfs(node, res):
            if node.left: dfs(node.left, res)
            if node.right: dfs(node.right, res)
            res.append(node.val)
        if not root: return []
        res = []
        dfs(root, res)
        return res

    #迭代写法
    #dfs是把左右子树加入以后再加入当前节点的值。迭代是先加当前节点的值再加左右子树的值。
    #所以需要反序一下。
    def postorderTraversal2(self, root):
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root.left: stack.append(root.left)
            if root.right: stack.append(root.right)
            res.append(root.val)
        return res[::-1]
