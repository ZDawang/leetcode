#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 239_Sliding_Window_Maximum.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #将当前nums[i]前比它小的值都删掉，因为不可能会是最大值
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        d = collections.deque()
        res = []
        for i in range(len(nums)):
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
        return res








