#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-3
#difficulty degree：
#problem: 300_Longest_Increasing_Subsequence
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(n2)
    #dp, 使用dp数组来存储到当前值得最大子序列
    def lengthOfLIS(self, nums):
        if not nums: return 0
        l = len(nums)
        dp = [0] * l
        for i in range(l):
            temp = 0
            #将小于当前值的结果+1的最大值作为当前值得结果
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j] + 1)
            dp[i] = max(temp, 1)
        return max(dp)

    #O(nlogn)
    #dp为到当前数字的最长数组，dp的长度不变小，当新数字来时，将新数字放入dp，隐性的做了一次len(dp) = max(len(dp), 到当前数字的最大子序列长度)
    def lengthOfLIS2(self, nums):
        if not nums: return 0
        l = len(nums)
        dp = [nums[0]] + [0] * (l - 1)
        size = 0
        for i in range(1, l):
            if nums[i] > dp[size]:
                dp[size + 1] = nums[i]
                size += 1
            else:
                #寻找大于等于当前num的最小值
                l, r = 0, size
                while(l < r):
                    m = l + (r - l) // 2
                    if dp[m] < nums[i]:
                        l = m + 1
                    else:
                        r = m
                dp[l] = nums[i]
        return size + 1


solute = Solution()
res = solute.lengthOfLIS2([3,5,6,2,5,4,19,5,6,7,12])
print(res)