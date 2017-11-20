#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-13
#difficulty degree：
#problem: 16_3Sum_closest
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def threeSumClosest(self, nums, target):
		nums.sort()
		len_nums = len(nums)
		if len_nums < 3:
			return 0
		res = sum(nums[:3])
		dis = abs(sum(nums[:3]) - target)
		for i in range(len_nums-2):
			if nums[i] > target//3:
				return res
			l, r = i+1, len_nums - 1
			while(l < r):
				temp = nums[i] + nums[l] + nums[r]
				print(i,l,r,temp,dis)
				if temp-target == 0:
					return temp
				if abs(temp - target) < dis:
					res = nums[i] + nums[l] + nums[r]
					dis = abs(temp - target)
				l, r = (l+1, r) if temp-target<0 else (l, r-1)
		return res

nums = [1,2,4,8,16,32,64,128]

solute = Solution()
res = solute.threeSumClosest(nums, 82)
print(res)