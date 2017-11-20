#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-3
#difficulty degree：
#problem: 199_Binary_Tree_Right_Side_View
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #层序遍历，找到每行最后一个值
    def rightSideView(self, root):
        if not root: return []
        queue = [root, "#"]
        res = []
        while queue:
            preroot = root
            root = queue.pop(0)
            if root == "#":
                if queue: queue.append("#")
                res.append(preroot.val)
                continue
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res