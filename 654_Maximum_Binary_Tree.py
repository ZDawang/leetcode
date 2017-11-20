#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-5
#difficulty degree：
#problem: 654_Maximum_Binary_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        index = nums.index(max(nums))
        node = TreeNode(nums[index])
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return node

