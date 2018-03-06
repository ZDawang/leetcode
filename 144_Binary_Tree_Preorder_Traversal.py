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

    def preorderTraversal4(self, root):
        #前驱节点与当前节点
        pre, cur = None, root   
        res = []
        while cur:
            #左孩子为空，输出当前节点，并转右孩子
            if not cur.left:    
                res.append(cur.val)
                cur = cur.right
            else:
                #寻找前驱节点
                pre = cur.left 
                while pre.right and pre.right != cur:
                    pre = pre.right
                #若前驱节点右孩子为空
                if not pre.right:
                    pre.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right
        return res

