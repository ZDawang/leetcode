#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 453_Minimum_Moves_to_Equal_Array_Elements
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def minMoves(self, nums):
        median = sorted(nums)[len(nums) / 2]
        return sum(abs(num - median) for num in nums)

nums = [1, 2, 3]
solute = Solution()
res = solute.minMoves(nums)
print(res)