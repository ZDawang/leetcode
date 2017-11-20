#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 109_Convert_Sorted_List_to_Binary_Search_Tree.py
#time_complecity:  
#space_complecity: 
#beats: 

#使用一个全局变量来控制移动，首先统计链表长度，确定结构，然后使用前序遍历的方式来进行树的构建
class Solution(object):
    def __init__(self):
        self.head = None
    def sortedListToBST(self, head):
        def dfs(l):
            if l == 0: return None
            if l == 1: 
                node = TreeNode(self.head.val)
                self.head = self.head.next
                return node

            n = (l - 1)//2
            node = TreeNode(0)
            node.left = dfs(l - 1 - n)
            node.val = self.head.val
            self.head = self.head.next
            node.right = dfs(n)
            return node

        self.head = head
        p, l = head, 0
        while p:
            p, l = p.next, l + 1

        return dfs(l)
        


