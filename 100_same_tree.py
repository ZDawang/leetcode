#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 100_same_tree
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
    #迭代
    def isSameTree(self, p, q):
        stack_p, stack_q = [], []
        while p or stack_p or q or stack_q:
            if (p and not q) or (q and not p):
                return False
            if p != None and q != None:
                if p.val != q.val:
                    return False
            if p:
                stack_p.append(p)
                p = p.left
            else:
                p = stack_p.pop()
                p = p.right

            if q:
                stack_q.append(q)
                q = q.left
            else:
                q = stack_q.pop()
                q = q.right
        return True

    #递归
    def isSameTree2(self, p, q):
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree2(p.left, q.left) and (self.isSameTree2(p.right, q.right))


p = TreeNode(0)
q = TreeNode(0)
solute = Solution()
res = solute.isSameTree(p, q)
print(res)