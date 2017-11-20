#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 637_Average_of_Levels_in_Binary_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def averageOfLevels(self, root):
        if not root: return []
        queue = [root, "#"]
        res = []
        mean = 0
        num = 0
        while queue:
            root = queue.pop(0)
            if root == "#":
                if queue: queue.append("#")
                res.append(float(mean) / num)
                mean, num = 0, 0
                continue
            mean, num = mean + root.val, num + 1
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res
