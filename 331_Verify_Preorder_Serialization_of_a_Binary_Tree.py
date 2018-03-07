#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 331_Verify_Preorder_Serialization_of_a_Binary_Tree.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用栈来进行验证。不是树的情况出现在：
    #当一个节点的左子树或者右子树还没构建，但是栈已经为空时，此时说明不是树
    def isValidSerialization(self, preorder):
        def dfs():
            #若栈为空，则说明不是树
            if not stack:
                return False
            #取出栈顶元素，若为"#"，则说明子树不需要构建，返回True
            val = stack.pop(0)
            if val == "#":
                return True
            #构建左右子树
            left = dfs()
            right = dfs()
            return left and right
        if not preorder:
            return False
        stack = preorder.split(",")
        #构建了一棵树并且栈为空
        return dfs() and (not stack)