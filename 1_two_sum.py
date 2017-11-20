#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-6
#difficulty degree ：easy
#problem:1.Two sum
#time_complecity: O(n)
#space_complecity: O(n)
#beats: 80.44
# 使用哈希（字典）寻找当前 target-当前数是否在字典中，在则结束
class Solution(object):
	def Two_Sum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		dic = {}
		for i in range(len(nums)):
			if target - nums[i] in dic:
				return (i, dic[target-nums[i]])
			dic[nums[i]] = i

nums = [1,3,4,5,7,8,9,11,15,18]
target = 29
a = 10
b = 0
c = a / b
solute = Solution()
print (solute.Two_Sum(nums,target))