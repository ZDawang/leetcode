#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-26
#difficulty degree：
#problem: 101_symmetric_tree
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
    #迭代,层序遍历,使用"#"分割每一层
    def isSymmetric(self, root):
        queue = [root, "#"]
        temp = []
        while queue:
            root = queue.pop(0)
            if root == "#":
                if queue: queue.append("#")
                for i in range(len(temp)//2):
                    if temp[i] != temp[-1 - i]:
                        return False
                temp = []
                continue
            if root == None:
                temp.append(None)
                continue
            queue.append(root.left)
            queue.append(root.right)
            temp.append(root.val)
        return True

    #递归,比较根节点的左子树与右节点的右子树是否对称，那么比较左子树的左子树与右子树的右子树以及
    #左子树的右子树与右子树的左子树是否同时相同
    def isSymmetric(self, root):
        def dfs(node1, node2):
            if node1 == None and node2 == None:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        if not root: return True
        return dfs(root.left, root.right)



        
nums = [0,1,2,2,3,4,4,3]
a = TreeNode(1)
root = a.GenerateTree(nums)

solute = Solution()
res = solute.isSymmetric(root)
print(res)

