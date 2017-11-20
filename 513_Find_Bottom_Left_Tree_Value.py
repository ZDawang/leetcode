#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 513_Find_Bottom_Left_Tree_Value
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #层序遍历的变形，先存右节点，再存左节点
    def findBottomLeftValue(self, root):
        if not root: return None
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root.right: queue.append(root.right)
            if root.left: queue.append(root.left)
        return root.val
