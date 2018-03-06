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

    #迭代写法，前序遍历改写。
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

    #前序遍历改写
    #后续遍历是根左右，前序是左右根，将前序改写为右左根，然后翻转结果即可。
    def postorderTraversal3(self, root):
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            root = stack.pop()
            root = root.left
        return res[::-1]


    def postorderTraversal4(self, root):
        #前驱节点与当前节点
        pre, cur = None, root   
        res = []
        while cur:
            #右孩子为空，输出当前节点，并转左孩子
            if not cur.right:    
                res.append(cur.val)
                cur = cur.left
            else:
                #寻找前驱节点
                pre = cur.right
                while pre.left and pre.left != cur:
                    pre = pre.left
                #若前驱节点左孩子为空
                if not pre.left:
                    res.append(cur.val)
                    pre.left = cur
                    cur = cur.right
                else:
                    pre.left = None
                    cur = cur.left
        return res[::-1]