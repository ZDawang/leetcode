#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 437_Path_Sum_III
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用sums保存到当前节点的所有可能累加结果，并统计以当前节点为截止节点的个数
    def pathSum(self, root, sum):
        def dfs(node, sums, sum):
            if not node: return 0
            newsums = sums + [0]
            res = 0
            for i in range(len(newsums)):
                newsums[i] += node.val
                if newsums[i] == sum: res += 1
            return res + dfs(node.left, newsums, sum) + dfs(node.right, newsums, sum)
        return dfs(root, [], sum)
