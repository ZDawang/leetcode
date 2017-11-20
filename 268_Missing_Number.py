#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5- 16
#difficulty degree：
#problem: 268_Missing_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #通过加法判断缺少的是哪个数
    def missingNumber(self, nums):
        l = len(nums)
        sum_nums = 0
        for i in range(l + 1):
            sum_nums += i
        res = sum_nums - sum(nums)
        return res



nums = [0,1, 2,3]
solute = Solution()
res = solute.missingNumber(nums)
print(res)