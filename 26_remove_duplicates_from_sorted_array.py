#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 26_remove_duplicates_from_sorted_array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def removeDuplicates(self, nums):
        len = 0
        num_early = None
        for num in nums:
            if num == num_early:
                continue
            nums[len] = num
            len = len+1
            num_early = num
        return len, nums[:len]

nums = [1,1,1,1,5,6,7]

solute = Solution()

res = solute.removeDuplicates(nums)

print(res)