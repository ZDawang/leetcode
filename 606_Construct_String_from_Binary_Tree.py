#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-5
#difficulty degree：
#problem: 606_Construct_String_from_Binary_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def tree2str(self, t):
        if t == None: return ""
        l, r = self.tree2str(t.left), self.tree2str(t.right)
        #当左子树为空时
        if l == "":
            return str(t.val) + "()" + "(" + r + ")" if r != "" else str(t.val)
        #当左子树不为空时
        return str(t.val) + "(" + l + ")" + "(" + r + ")" if r != "" else str(t.val) + "(" + l + ")"

