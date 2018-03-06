#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-14
#difficulty degree：
#problem: 94_binary_tree_inorder_traversal
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
    #递归
    def inorderTraversal(self, root):
        def dfs(node):
            if node.left: dfs(node.left)
            res.append(node.val)
            if node.right: dfs(node.right)
        if not root: return []
        res = []
        dfs(root)
        return res 

    #迭代
    def inorderTraversal2(self, root):
        stack = []
        res = []
        while root or stack:
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal3(self, root):
        #前驱节点与当前节点
        pre, cur = None, root   
        res = []
        while cur:
            #左孩子为空，输出当前节点，并转右孩子
            if not cur.left:    
                res.append(cur.val)
                cur = cur.right
            else:
                #寻找前驱节点
                pre = cur.left 
                while pre.right and pre.right != cur:
                    pre = pre.right
                #若前驱节点右孩子为空
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    pre.right = None
                    cur = cur.right
        return res


nums = [0,1,2,3,4,5,6,7] 
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.inorderTraversal2(root)
print(res)
