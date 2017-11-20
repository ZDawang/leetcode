#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 450_Delete_Node_in_a_BST
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #找到当前key的节点后，选择比它大的最小值x来代替它，然后删除x。循环此操作。
    def deleteNode(self, root, key):
        if root == None: return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right: return root.left
            if not root.left: return root.right
            root.val = self.findminnum(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root

    def findminnum(self, root):
        minnum = root.val
        while root.left:
            root = root.left
            minnum = root.val
        return minnum

