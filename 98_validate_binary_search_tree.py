#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-24
#difficulty degree：
#problem: 98_validate_binary_search_tree
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
    def isValidBST(self, root):
        stack = []
        res = []
        while root or stack:
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        for i in range(len(res) - 1):
            if res[i + 1] <= res[i]:
                return False
        return True

nums = [0,1,2,3,4,5,6,7]
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.isValidBST(root)
print(res)
