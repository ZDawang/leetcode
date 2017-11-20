#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 515_Find_Largest_Value_in_Each_Tree_Row
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #层序遍历
    def largestValues(self, root):
        if not root: return []
        res = []
        queue = [root, "#"]
        maxnum = root.val
        while queue:
            root = queue.pop(0)
            if root == "#":
                if queue: queue.append("#")
                res.append(maxnum)
                maxnum = float("-inf")
                continue
            maxnum = max(maxnum, root.val)
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res