#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 154_Find_Minimum_in_Rotated_Sorted_Array_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(n)
    def findMin(self, nums):
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]

    #O(logn)
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while(l <= r):
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = l + (r - l)//2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

nums = [3, 1]
solute = Solution()
res = solute.findMin(nums)
print(res)