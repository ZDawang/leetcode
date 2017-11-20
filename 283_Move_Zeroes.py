#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #冒泡
    def moveZeroes2(self, nums):
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                for j in range(i + 1, l):
                    if nums[j] == 0:
                        continue
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

    #从头开始放非0的数值
    def moveZeroes(self, nums):
        last0 = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[i], nums[last0] = nums[last0], nums[i]
                last0 += 1
                print(nums)

nums = [1, 0, 0, 3, 12]
solute = Solution()
res = solute.moveZeroes(nums)
print(nums)
