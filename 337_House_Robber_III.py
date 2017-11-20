#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 337_House_Robber_III
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def rob(self, root):
        def dfs(node, prestate):
            if not node: return 0
            notrob = dfs(node.left, 0) + dfs(node.right, 0)
            rob = dfs(node.left, 1) + dfs(node.right, 1) + node.val
            if prestate == 1:
                return notrob
            else:
                return max(rob, notrob)
        if not root: return 0
        return max(dfs(root.left, 0) + dfs(root.right, 0), dfs(root.left, 1) + dfs(root.right, 1) + root.val)

    #DP+dfs,返回每个节点的抢与不抢的最大值
    def rob(self, root):
        def dfs(node):
            if not node: return 0, 0
            lrob, lnotrob = dfs(node.left)
            rrob, rnotrob = dfs(node.right)
            currob = lnotrob + rnotrob + node.val
            curnotrob = max(lrob, lnotrob) + max(rrob, rnotrob)
            return currob, curnotrob
        return max(dfs(root))