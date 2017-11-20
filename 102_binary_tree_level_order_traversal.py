#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-26
#difficulty degree：
#problem: 102_binary_tree_level_order_traversal
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
    #层序遍历
    def isSymmetric(self, root):
        res = []
        queue = [root]
        while queue:
            temp = []
            queue.append("#")
            while True:
                q = queue.pop(0)
                if q =="#":
                    break
                if q == None:
                    continue
                print(q.val)
                temp.append(q.val)
                queue.append(q.left)
                queue.append(q.right)
            res.append(temp)
        res.pop()
        return res


nums = [0,1,2,2,0,4,4,3]
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.isSymmetric(root)
print(res)

