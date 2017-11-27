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


    #双指针
    #一个指针从前向后代表非val的位置，一个指针从后向前代表val的位置。
    def removeElement(self, nums, val):
        nump, valp = 0, len(nums) - 1
        while nump <= valp:
            while nums[nump] == val and nump <= valp:
                nums[nump], nums[valp] = nums[valp], nums[nump]
                valp -= 1
            nump += 1
        #valp位置仍不是val，所以长度为valp+1
        return valp + 1




nums = [2,2,4,5,6,2,7]
solute = Solution()
res = solute.removeElement(nums, 2)

print(res)