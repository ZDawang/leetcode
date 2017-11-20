#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 78_subsets
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def subsets(self, nums):
        def dfs(nums, l_temp, l, res):
            len_nums = len(nums)
            res.append(l_temp)
            if l >= len_nums:
                return
            for i in range(l, len_nums):
                dfs(nums, l_temp + [nums[i]], i + 1, res)
        res = [[]]
        for i in range(len(nums)):
            dfs(nums[i + 1:], [nums[i]], 0, res)
        return res
    def subsets2(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

nums = [1,2,5]
solute = Solution()
res = solute.subsets2(nums)
print(res)
