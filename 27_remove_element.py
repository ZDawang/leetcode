#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 27_remove_element
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def removeElement(self, nums, val):
        len = 0
        for num in nums:
            if num == val:
                continue
            nums[len] = num
            len = len+1
            num_early = num
        return len, nums[:len]

nums = [2,2,4,5,6,2,7]
solute = Solution()
res = solute.removeElement(nums, 2)

print(res)