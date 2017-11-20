#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 530_Minimum_Absolute_Difference_in_BST
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def getMinimumDifference(self, root):
        def findbignum(root):
            if not root or not root.right: return float("inf")
            root = root.right
            while root.left:
                root = root.left
            return root.val
        def findsmallnum(root):
            if not root or not root.left: return float("inf")
            root = root.left
            while root.right:
                root = root.right
            return root.val

        if not root: return float("inf")
        bigval, smallval = findbignum(root), findsmallnum(root)
        return min(abs(root.val - bigval), abs(root.val - smallval), self.getMinimumDifference(root.left), self.getMinimumDifference(root.right))

