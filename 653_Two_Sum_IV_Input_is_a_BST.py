#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 653_Two_Sum_IV_Input_is_a_BST
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #two point
    def findTarget(self, root, k):
        if not root: return False
        posstack, revstack = [], []
        revroot = root
        #将两点分别放在最大与最小值
        while root:
            posstack.append(root)
            root = root.left
        while revroot:
            revstack.append(revroot)
            revroot = revroot.right
        root = posstack.pop()
        revroot = revstack.pop()

        while(root.val < revroot.val):
            if root.val + revroot.val == k: return True
            if root.val + revroot.val < k:
                root = root.right
                while root:
                    posstack.append(root)
                    root = root.left
                root = posstack.pop()
            else:
                revroot = revroot.left
                while revroot:
                    revstack.append(revroot)
                    revroot = revroot.right
                revroot = revstack.pop()
        return False

