#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 80_remove_duplicates_from_sorted_array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def removeDuplicates(self, nums):
        index = 1
        count = 0
        for i in range(1, len(nums)):
            #遍历，当第一次等于时以及不等于时，赋值
            if nums[i] == nums[i - 1]:
                if count == 0:
                    count = 1
                    nums[index] = nums[i]
                    index += 1
            else:
                nums[index] = nums[i]
                index += 1
                count = 0
        return index if nums else 0

nums = []
solute = Solution()
res = solute.removeDuplicates(nums)

print(nums)
print(res)
print(nums[:res])
