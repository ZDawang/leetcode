#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 538_Convert_BST_to_Greater_Tree4
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #前序遍历一遍，得到累加结果，再重新赋值
    #或者
    def convertBST(self, root):
        if root == None: return None
        res = root
        sumnum = 0
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                #或者这里改为root = root.right,这样就可以不用迭代两次了
                root = root.left
            root = stack.pop()
            sumnum += root.val
            root = root.right
        root = res
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            sumnum, root.val = sumnum - root.val, sumnum
            root = root.right
        return res

        
