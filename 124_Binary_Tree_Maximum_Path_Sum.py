#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-3
#difficulty degree：
#problem: 124_Binary_Tree_Maximum_Path_Sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #对每一个node，查看其包含当前节点的最大值，在这些最大值中找出最大值
    #对每一个节点，有两种操作，第一个是选择左子树与右子树的最大值，供上面的节点使用，另一个是把当前节点作为最高节点，计算最大值
    def maxPathSum(self, root):
        def dfs(node, res):
            if not node: return 0
            lsum = dfs(node.left, res)
            rsum = dfs(node.right, res)
            ltmp = lsum + node.val if lsum > 0 else node.val
            rtmp = rsum + node.val if rsum > 0 else node.val
            tmp = ltmp + rtmp - node.val
            res[0] = max(res[0], tmp)
            return max(ltmp, rtmp)
        if not root: return 0
        res = [float("-inf")]
        dfs(root, res)
        return res[0]