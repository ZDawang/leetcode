#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-26
#difficulty degree：
#problem: 104_maximum_depth_of_binary_tree
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
    def maxDepth(self, root):
        if not root:
            return 0
        res, queue = 0, [root]
        while queue:
            for i in range(len(queue)):
                q = queue.pop(0)
                if q.left : queue.append(q.left)
                if q.right : queue.append(q.right)
            res += 1
        return res


nums = [0,1,0,2]
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.maxDepth(root)
print(res)
