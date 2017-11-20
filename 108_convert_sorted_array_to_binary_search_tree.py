#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-4-26
#difficulty degree：
#problem: 108_convert_sorted_array_to_binary_search_tree
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
    def sortedArrayToBST(self, nums):
        def dfs(nums, start, end):
            if start > end: return None
            mid = (start + end)//2
            newnode = TreeNode(nums[mid])
            newnode.left = dfs(nums, start, mid - 1)
            newnode.right = dfs(nums, mid + 1, end)
            return newnode
        root = dfs(nums, 0, len(nums) - 1)
        return root
        

nums = [1,3]

solute = Solution()
root = solute.sortedArrayToBST(nums)
print(root.left.val)