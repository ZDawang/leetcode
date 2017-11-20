#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-15
#difficulty degree：
#problem: 95_unique_binary_search_trees_II
#time_complecity:  
#space_complecity: 
#beats: 


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def CreateTree(self, tree, nums, i):
        if i >= len(nums) // 2:
            return
        if nums[2 * i] != 0:
            tree.left = TreeNode(nums[2 * i])
            self.CreateTree(tree.left, nums, 2*i)
        if nums[2 * i + 1] != 0:
            tree.right = TreeNode(nums[2 * i + 1])
            self.CreateTree(tree.right, nums, 2*i + 1)

    def GenerateTree(self, nums):
        root = TreeNode(nums[1])
        self.CreateTree(root, nums, 1)
        return root


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n+1)
        
    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result

    #DP
    def generateTrees2(self, n):
        def clone(node, offset):
            if not node: return None
            newnode = TreeNode(offset + node.val)
            newnode.left = clone(node.left, offset)
            newnode.right = clone(node.right, offset)
            return newnode

        if n == 0: return []
        dp = [[] for i in range(n + 1)]
        dp[0], dp[1] = [None], [TreeNode(1)]
        for i in range(2, n + 1):
            for j in range(i):
                for node1 in dp[j]:
                    for node2 in dp[i - j - 1]:
                        newnode = TreeNode(j + 1)
                        newnode.left = clone(node1, 0)
                        newnode.right = clone(node2, j + 1)
                        dp[i].append(newnode)
        return dp[-1]



        

solute = Solution()
res = solute.generateTrees(3)
print(res[1].right.val)