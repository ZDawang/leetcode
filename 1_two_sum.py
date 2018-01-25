#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-6
#difficulty degree ：easy
#problem:1.Two sum
#time_complecity: O(n)
#space_complecity: O(n)
#beats: 80.44

class Solution(object):
    #哈希表
    def Two_Sum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            d[num] = i
        return

    #排序+双指针
    def Two_Sum(self, nums, target):
        nums = sorted([num, i] for i, num in enumerate(nums))
        l, r = 0, len(nums) - 1
        while l < r:
            sums = nums[l][0] + nums[r][0]
            if sums == target:
                return [nums[l][1], nums[r][1]]
            elif sums < target:
                l += 1
            else:
                r -= 1
        return



nums = [1,3,4,5,7,8,9,11,15,18,20]
target = 29
a = 10
b = 0
c = a / b
solute = Solution()
print (solute.Two_Sum(nums,target))