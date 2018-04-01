#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-12
#difficulty degree：
#problem: 81_search_in_rotated_sorted_array_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r and nums[l] == nums[l + 1]:
            l += 1
        while l < r and nums[r] == nums[r - 1]:
            r -= 1
        while(l <= r):
            middle = (l + r)//2
            if nums[middle] == target or nums[r] == target:
                return True
            if nums[l]  < nums[middle]:
                if nums[l]  <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if nums[middle]  <= target < nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
        return False


    def search2(self, nums, target):
        if not nums: return False
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            elif nums[m] > nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                r -= 1
        return nums[l] == target



nums = [1,1,1,1]
target = 3

solute = Solution()
res = solute.search(nums, target)

print(res)