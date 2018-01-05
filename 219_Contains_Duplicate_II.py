#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 219_Contains_Duplicate_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            else:
                d[nums[i]] = i
        return False

    #滑动窗
    #用window来存放长度为k的数。(刚开始时，长度小于k)。
    #检测当前数是否在窗中即可。
    #l,r为窗的边界。
    def containsNearbyDuplicate2(self, nums, k):
        if not nums or k == 0:
            return False
        window, l = set(), 0
        for r, num in enumerate(nums):
            if num in window:
                return True
            if r - l == k:
                window.remove(nums[l])
                l += 1
            window.add(num)
        return False