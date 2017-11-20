#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 33_search_in_rotated_sorted_array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            if nums[right] == target:
                return right
            if nums[left]  < nums[middle]:
                if nums[left]  <= target < nums[middle]:
                    left = left
                    right = middle - 1
                else:
                    left = middle + 1
                    right = right
            else:
                if nums[middle]  <= target < nums[right]:
                    left = middle + 1
                    right = right
                else:
                    left = left
                    right = middle - 1
        return -1

nums = [6,1,2,3,4,5]
target = 5

solute = Solution()
res = solute.search(nums, target)

print(res)