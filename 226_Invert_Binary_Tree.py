#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #递归
    def invertTree(self, root):
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    #迭代,遍历一遍
    def invertTree2(self, root):
        if not root: return None
        res = root
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
            root.left, root.right = root.right, root.left
        return res
