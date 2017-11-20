#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-3
#difficulty degree：
#problem: 236_Lowest_Common_Ancestor_of_a_Binary_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #分两种情况，第一种是p，q在左右支树，第二种是p在q的子树中
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root, p, q, res):
            if root == None: return False
            ls, rs = dfs(root.left, p, q, res), dfs(root.right, p, q, res)
            if root == q or root == p:
                if ls or rs: res[0] = root
                return True
            if ls and rs: res[0] = root
            return (ls or rs)

        res = [root]
        dfs(root, p, q, res)
        return res[0]