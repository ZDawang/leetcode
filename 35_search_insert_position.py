#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 35_search_insert_position
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #遍历
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert2(self, nums, target):
        #二分法
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target <= nums[mid + 1]:
                return mid + 1
            if target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return len(nums)


nums = [1,3,5]
target = 2

solute = Solution()
res = solute.searchInsert2(nums, target)

print(res)