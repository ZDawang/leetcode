#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 53_maximum_subarray
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def maxSubArray(self, nums):
        res = nums[0]
        for i in range(len(nums)):
            temp = nums[i]
            if temp > res:
                    res = temp
            for j in range(i + 1, len(nums)):
                temp += nums[j]
                if temp > res:
                    res = temp
        return res


    def maxSubArray2(self, nums):
        #从左往右找，因为最终结果左边的数据之和肯定是小于0的，所以当累加和小于0，就移动l值
        l, temp, res = 0, 0, nums[0]
        for i in range(len(nums)):
            temp += nums[i]
            while (temp < nums[i]) and (l < i):
                temp -= nums[l]
                l += 1
            res = max(res, temp)
        return res

    #DP
    def maxSubArray3(self, nums):
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = num + max(0, dp[i - 1])
        return max(dp)

nums = [-2,-1]

solute = Solution()

res = solute.maxSubArray2(nums)
print(res)
