#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 368_Largest_Divisible_Subset.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        temp = [1]
        d = {}
        max_res = 0
        index_res = 0
        for i in range(1, len(nums)):
            max_l = 1
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if (temp[j] + 1) > max_l:
                        max_l = temp[j] + 1
                        d[i] = j
            temp.append(max_l)
            if max_l > max_res:
                max_res = max_l
                index_res = i
        res = []
        while(index_res in d):
            res.append(nums[index_res])
            index_res = d[index_res]
        res.append(nums[index_res])
        return res[::-1]


solute = Solution()
nums = [1, 2, 3]
res = solute.largestDivisibleSubset(nums)
print(res)
