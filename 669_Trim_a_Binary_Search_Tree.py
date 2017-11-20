#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 669_Trim_a_Binary_Search_Tree.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def trimBST(self, root, L, R):
        if not root: return None
        #当前节点的值比R大时，所需要的节点都在左侧
        if root.val > R:
            return self.trimBST(root.left, L, R)
        #前节点的值比R小时，所需要的节点都在右侧
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        #整理左右子树，返回当前节点
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root