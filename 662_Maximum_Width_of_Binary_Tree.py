#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-5
#difficulty degree：
#problem: 662_Maximum_Width_of_Binary_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        left, curdepth, res = 0, 0, 0
        while queue:
            node, depth, pos = queue.pop(0)
            if node:
                if curdepth != depth:
                    curdepth, left = depth, pos
                res = max(res, pos - left + 1)
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
        return res




