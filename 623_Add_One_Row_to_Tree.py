#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-5
#difficulty degree：
#problem: 623_Add_One_Row_to_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #层序遍历
    def addOneRow(self, root, v, d):
        if d == 1:
            newroot = TreeNode(v)
            newroot.left = root
            return newroot
        res = root
        queue = [root, "#"]
        depth = 2
        while queue:
            root = queue.pop(0)
            if root == "#":
                if queue: queue.append("#")
                depth += 1
                if depth == d + 1:
                    return res
                continue
            if depth == d:
                lnewnode = TreeNode(v)
                rnewnode = TreeNode(v)
                root.left, lnewnode.left = lnewnode, root.left
                root.right, rnewnode.right = rnewnode, root.right
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res
