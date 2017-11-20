#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 307_Range_Sum_Query_Mutable.py
#time_complecity:  
#space_complecity: 
#beats: 

#BIT
#一个注意的地方是原有BIT的下标是1-n的，现在是0-n-1的，所以在计算low_bit时，要进行+1操作
class NumArray(object):
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l
        #构建初始树
        for i, num in enumerate(nums):
            while i < self.l:
                self.tree[i] += num
                i += self.lowbit(i + 1)

    #更新值，先计算原来的值，在把差值更新
    def update(self, i, val):
        numi = self.sumRange(i, i)
        diff = val - numi
        while i < self.l:
            self.tree[i] += diff
            i += self.lowbit(i + 1)

    #计算下标i所对应的范围
    def lowbit(self, i):
        return i & (-i)

    #先计算0-i-1的和，再计算0-j的和，再算差值
    def sumRange(self, i, j):
        sumi, sumj = 0, 0
        i -= 1
        while i >= 0:
            sumi += self.tree[i]
            i -= self.lowbit(i + 1)

        while j >= 0:
            sumj += self.tree[j]
            j -= self.lowbit(j + 1)
        return sumj - sumi


class SegTreeNode(object):
    def __init__(self, leftVal, rightVal):
        self.leftVal = leftVal
        self.rightVal = rightVal
        self.left = None
        self.right = None
        self.sums = 0

#segment tree
class NumArray(object):
    def __init__(self, nums):
        self.root = self.CreateTree(nums, 0, len(nums) - 1)

    def CreateTree(self, nums, l, r):
        if l > r:
            return None
        if l == r:
            node = SegTreeNode(l, r)
            node.sums = nums[l]
            return node
        m = (l + r) // 2
        root = SegTreeNode(l, r)
        root.left = self.CreateTree(nums, l, m)
        root.right = self.CreateTree(nums, m + 1, r)
        root.sums = root.left.sums + root.right.sums
        return root

    def update(self, i, val):
        self.updateHelper(self.root, i, val)

    def updateHelper(self, root, i, val):
        if root.leftVal == root.rightVal:
            root.sums = val
            return val
        m = (root.leftVal + root.rightVal)//2

        if i <= m:
            self.updateHelper(root.left, i, val)
        else:
            self.updateHelper(root.right, i, val)

        root.sums = root.left.sums + root.right.sums
        return root.sums

    def sumRange(self, i, j):
        return self.sumRangeHelper(self.root, i, j)

    def sumRangeHelper(self, root, i, j):
        if root.leftVal == i and root.rightVal == j:
            return root.sums
        m = (root.leftVal + root.rightVal)//2
        if j <= m:
            return self.sumRangeHelper(root.left, i, j)
        elif i >= m + 1:
            return self.sumRangeHelper(root.right, i, j)
        else:
            return self.sumRangeHelper(root.left, i, m) + self.sumRangeHelper(root.right, m + 1, j)


nums = [1, 3, 5]
NA = NumArray(nums)
sums = NA.sumRange(0, 2)
