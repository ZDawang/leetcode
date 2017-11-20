#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-26
#difficulty degree：
#problem: 107_binary_tree_level_order_traversal_II
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
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            for i in range(len(queue)):
                q = queue.pop(0)
                if q.left : queue.append(q.left)
                if q.right : queue.append(q.right)
                temp += [q.val]
            res += [temp]
        res.reverse()
        return res


nums = [0,3,9,20,0,0,15,7]
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.levelOrderBottom(root)
print(res)
