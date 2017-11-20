#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 560_Subarray_Sum_Equals_K
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #初始思路：排序后计算：复杂度过高 O（nlogn），应该有O（n）解决方法
    #用字典存储累加到当前值得和，若当前值的和-k在字典中，则说明有解决方案, 非DP
    def subarraySum(self, nums, k):
        res = 0
        sum_temp = 0
        d = {0 : 1}
        for i in range(len(nums)):
            sum_temp += nums[i]
            res += d.get(sum_temp - k, 0)
            d[sum_temp] = d.setdefault(sum_temp, 0) + 1
        return res


nums = [1]
solute = Solution()
res = solute.subarraySum(nums, 0)
print(res)
