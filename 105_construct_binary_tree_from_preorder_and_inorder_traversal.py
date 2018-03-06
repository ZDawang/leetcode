#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-26
#difficulty degree：
#problem: 105_construct_binary_tree_from_preorder_and_inorder_traversal
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
    def buildTree(self, preorder, inorder):
        if inorder:
            x = preorder.pop(0)
            root = TreeNode(x)
            index = inorder.index(x)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root

    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = preorder[0]
        idx = inorder.index(root)
        node = TreeNode(root)
        node.left = self.buildTree(preorder[1: idx+1], inorder[:idx])
        node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return node

