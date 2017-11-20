#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3- 25
#difficulty degree：
#problem: 34_search_for_a_range
#time_complecity:  
#space_complecity: 
#beats: 93

class Solution(object):
    def searchRange(self, nums, target):
        #分别寻找两个数，两个二分法同时进行：
        #寻找左出发点
        l = len(nums)
        l1, l2, r1, r2 = 0, 0, l - 1, l - 1
        l_index, r_index = 0, 0
        if l == 0:
            return [-1, -1]
        if nums[0] == nums[-1]:
            if nums[0] == target:
                return[0, l - 1]
        while(l1 <= r1):
            mid1 = (l1 + r1)//2
            if (nums[mid1] != target or nums[mid1] == nums[mid1 - 1]):
                if nums[mid1] < target:
                    l1 = mid1 + 1
                else:
                    r1 = mid1 - 1
            else:
                l_index = 1
                break
        mid1 = mid1 if l_index else -1
        #寻找右出发点
        while(l2 <= r2):
            mid2 = (l2 + r2)//2
            if (nums[mid2] != target or nums[mid2] == nums[(mid2 + 1)%l]):
                if nums[mid2] <= target:
                    l2 = mid2 + 1
                else:
                    r2 = mid2 - 1
            else:
                r_index = 1
                break
        mid2 = mid2 if r_index else -1
        return [mid1, mid2]



nums = []

solute = Solution()

res = solute.searchRange(nums, 2)

print(res)