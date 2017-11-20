#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 687_Longest_Univalue_Path.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #对于一个节点，有两种情况，一种是当前节点作为根节点。结果为左子树结果+右子树结果
    #另一种情况是，作为子树中的节点，根节点在上层。
    #使用dfs.res来比较所有节点作为根节点的值。选出最大值。
    def longestUnivaluePath(self, root):
        def dfs(node):
            if not node: return 0, 0
            #获得左右子树的值与数量
            leftval, leftnum = dfs(node.left)
            rightval, rightnum = dfs(node.right)
            val = node.val
            #当前节点作为根节点
            dfs.res = max(dfs.res, leftnum * (val == leftval) + rightnum * (val == rightval))
            #作为子树时的最大长度
            num = max(leftnum * (val == leftval), rightnum * (val == rightval)) + 1
            return val, num

        dfs.res = 0
        dfs(root)
        return dfs.res