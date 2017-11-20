#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-3
#difficulty degree：
#problem: 230_Kth_Smallest_Element_in_a_BST
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #中序遍历，BST的中序遍历为已排序好的升序。
    def kthSmallest(self, root, k):
        stack = []
        count = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            count += 1
            if count == k: return root.val
            root = root.right
        return None

