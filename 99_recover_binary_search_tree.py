#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-24
#difficulty degree：
#problem: 99_recover_binary_search_tree
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
    #中序遍历，找出两个异常值，然后交换
    #第一个异常值肯定比后面的数大，第二个异常值肯定比前面的数小
    #所以只需要跟前面的数相比较,第一次找到的节点为数大的节点，第二次找到的节点为数小的节点
    def recoverTree(self, root):
        stack = []
        prenode = TreeNode(float("-inf"))
        node1, node2, tmp = None, None, None
        #中序遍历
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            #判断是哪个节点
            if root.val < prenode.val:
                if not node1:
                    node1 = prenode
                    tmp = root
                else:
                    node2 = root
                    break
            prenode = root
            root = root.right
        #判断是否为相邻节点的情况
        node2 = node2 if node2 else tmp
        node1.val, node2.val = node2.val, node1.val