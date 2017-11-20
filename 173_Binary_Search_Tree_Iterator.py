#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 173_Binary_Search_Tree_Iterator.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def __init__(self, root):
        self.stack = []
        self.root = root

    def hasNext(self):
        return False if (not self.stack and not self.root) else True

    def next(self):
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        res = self.root.val
        self.root = self.root.right
        return res
            

