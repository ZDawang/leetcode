#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 84_Largest_Rectangle_in_Histogram.py
#time_complecity:  
#space_complecity: 
#beats: 
import queue
class Solution(object):
    #第一种思路,因为面积由长宽确定，宽度是下标差，长度就是最短的矩形，所以遍历一下即可
    #不出意外TLE。
    def largestRectangleArea(self, heights):
        res = 0
        l = len(heights)
        for i in range(l):
            minheight = heights[i]
            for j in range(i, l):
                minheight = min(minheight, heights[j])
                res = max(res, minheight * (j - i + 1))
        return res

    #stack，stack中只存储比当前低的矩形，这样就可以减少运算量，不用遍历所有的矩形
    #因为加了一个0，所以最后stack会清空。最终的stack=[-1]
    #因为所有的height都入栈出栈过，所以对于每个height，都计算了一遍其对应的最大面积。
    #O(n)
    def largestRectangleArea2(self, heights):
        stack, res = [-1], 0
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                #因为stack是递增的，所以从stack[-1]+1到stack.pop()，高度都大于等于h的
                #因为stack是递增的，所以从stack.pop()到i-1，高度都是大于等于h的，不然stack.pop()早就被移出栈了
                #且因为stack[-1]的高度是小于h的，i的高度也是小于h的。所以h对应的最大宽度就是下面w的计算公式
                h = heights[stack.pop()]
                w = (i - 1) - (stack[-1] + 1) + 1
                #w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

    #O(n)，更容易理解版本
    #记录左边比当前低的最大值，右边比当前低的最小值。计算面积
    def largestRectangleArea3(self, heights):
        l = len(heights)
        left, right = [-1] * l, [l] * l
        #维持一个严格递增的栈,找到左边最近的比当前height低的下标
        stack = []
        for i in range(l):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)
        #跟查找左边的类似，只需要倒着查找就可以了, 找到右边最近的比当前height低的下标
        stack = []
        for i in range(l - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right[i] = l if not stack else stack[-1]
            stack.append(i)
        #计算结果
        #从left[i]+1 到right[i]-1
        res = 0
        for i in range(l):
            res = max(res, ((right[i] - 1) - (left[i] + 1) + 1) * heights[i])
        return res




heights = [1,1,1,1,1]
solute = Solution()
res = solute.largestRectangleArea3(heights)
