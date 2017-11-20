#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-12
#difficulty degree：
#problem: 15_3sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution1(object):
	#先创建一个两个数之和的哈希列表，再遍历数组，寻找它每个元素的负数所对应的字典中的另外两个数的值
	def threeSum(self, nums):
		two_dim_dic = {}
		res = []
		if len(nums) < 3:
			return [[]]
		for i in range(len(nums)):
			for j in range(len(nums)):
				if j<i:
					if (nums[i] + nums[j]) in two_dim_dic :
						two_dim_dic[nums[i] + nums[j]].append([nums[i], nums[j], i, j])
					else:
						two_dim_dic[nums[i] + nums[j]] = [[nums[i], nums[j], i, j]]
		for k in range(len(nums)):
			if -nums[k] in two_dim_dic:
				for l in two_dim_dic[-nums[k]]:
					if not(([nums[k], l[0], l[1]] in res) or ([nums[k], l[1], l[0]] in res) or ([l[1], nums[k], l[0]] in res) 
						or ([l[1], l[0], nums[k]] in res) or ([l[0], nums[k], l[1]] in res) or ([l[0], l[1], nums[k]] in res)):
						res.append([nums[k]] + l[:2])
		return res

class Solution2(object):
	def threeSum(self, nums):
		res = []

		nums.sort()
		len_nums = len(nums)
		for i in range(len_nums - 2):
			if sums[i] > 0:
				return res
			if i>0 and nums[i] == nums[i-1]:
				continue
			l, r = i+1, len_nums -1
			while(l < r):
				s = nums[i] + nums[l] + nums[r]
				if s < 0:
					l += 1
				elif s > 0:
					r -= 1
				else:
					res.append([nums[i], nums[l], nums[r]])
					while(l<r and nums[l] == nums[l+1]):
						l += 1
					while(l<r and nums[r] == nums[r-1]):
						r -= 1
					l += 1
					r -= 1
		return res


class Solution(object):
	#固定一个数，将问题转化为two sum
	def threeSum(self, nums):
		nums.sort()

		res =[]
		len_nums = len(nums)
		if len_nums < 3 :
			return res
		d = {}
		for i in range(len_nums):
			d[nums[i]] = i
		for i in range(len_nums - 2):
			if i>0 and nums[i] == nums[i-1]:
				continue
			if nums[i] > 0:
				return res
			j = i + 1
			while(nums[j] < -nums[i]/2 and j < len_nums -1):
				if -nums[i]-nums[j] in d:
					if d[-nums[i]-nums[j]] > j:
						res.append([nums[i], nums[j], -nums[i]-nums[j]])
				j += 1
		return res

class Solution3(object):
	def threeSum(self, nums):
		nums.sort()
		res =[]
		len_nums = len(nums)
		if len_nums < 3 :
			return res
		d = {}
		for i in range(len_nums):
			d[nums[i]] = i
		for i in range(len_nums - 2):
			if i>0 and nums[i] == nums[i-1]:
				continue
			if nums[i] > 0:
				return res
			j = i + 1
			while(nums[j] <= -nums[i]/2 and j < len_nums - 1):
				if -nums[i]-nums[j] in d:
					if d[-nums[i]-nums[j]] > j:
						res.append([nums[i], nums[j], -nums[i]-nums[j]])
				while nums[j] == nums[j + 1] and j < len_nums -2:
					j = j + 1
				j += 1
		return res


nums = [0,0,0,0]

solute = Solution3()
res = solute.threeSum(nums)

print(res)