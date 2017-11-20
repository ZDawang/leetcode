#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-24
#difficulty degree：
#problem: 96_unique_binary_search_trees
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
    #TLE
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        fn = 0
        for i in range(n//2):
            fn += self.numTrees(i)*self.numTrees(n - 1 - i)*2
        if n%2 == 1:
            fn += self.numTrees(n//2)*self.numTrees(n//2)
        return fn

    def numTrees2(self, n):
        if n == 0:
            return 1
        if n == 1 or n == 2:
            return n
        num = [0 for i in range(n + 1)]
        num[0] = num[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                num[i] += num[j] * num[i - j - 1]
        return num[n]




solute = Solution()
res = solute.numTrees2(3)
print(res)