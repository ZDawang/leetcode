#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-26
#difficulty degree：
#problem: 103_binary_tree_zigzag_level_order_traversal
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
    def zigzagLevelOrder(self, root):
        res = []
        queue = [root]
        reverse = 0
        while queue:
            temp = []
            queue.append("#")
            while True:
                q = queue.pop(0)
                if q =="#":
                    break
                if q == None:
                    continue
                temp.append(q.val)
                queue.append(q.left)
                queue.append(q.right)
            if reverse:
                temp.reverse()
            res.append(temp)
            reverse = (reverse + 1)%2
        res.pop()
        return res
        
    def zigzagLevelOrder2(self, root):
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in range(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res

nums = [0,3,9,20,0,0,15,7]
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.zigzagLevelOrder(root)
print(res)
