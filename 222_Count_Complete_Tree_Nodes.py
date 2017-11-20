#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-3
#difficulty degree：
#problem: 222_Count_Complete_Tree_Nodes
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #最基本思路：遍历数一遍, TLE
    def countNodes(self, root):
        if not root: return 0
        queue = [root]
        res = 0
        while queue:
            root = queue.pop(0)
            res += 1
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res

    #log(n)思路，只有深度有关
    #检测一个节点的左右子树的深度，若相同则左子树是一个perfect二叉树，不用再看
    def countNodes(self, root):
        def height(node):
            if not node: return 0
            return height(node.left) + 1

        if not root: return 0
        l, r = height(root.left), height(root.right)
        if l == r:
            #2**l = 2**0 + 2 ** 1 +... + 2**(l-1) + 1
            return 2 ** l + self.countNodes(root.right)
        else:
            return 2 ** r + self.countNodes(root.left)

