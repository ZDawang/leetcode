#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 673_Number_of_Longest_Increasing_Subsequence.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用length, number存储到当前数字的最长子串长度及 最长子串个数。
    #O(n2)
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        n = len(nums)
        length, number = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                #若由j的子串长度更长
                if length[i] <= length[j]:
                    length[i] = length[j] + 1
                    number[i] = number[j]
                #若由j的子串跟i的子串一样长。
                elif length[i] == length[j] + 1:
                    number[i] += number[j]
        maxlength = max(length)
        return sum(number[i] for i in range(n) if length[i] == maxlength)

    #可以做优化，像300题一样。
    #O(nlogn)
    #dp[i]表示长度为i的递增子串的结尾最小数字。
    #count[i][num] 表示长度为i的递增子串的结尾为num的子串数量。
    def findNumberOfLIS2(self, nums):
        #在nums中找到比当前数字大一点的数字。
        def binarySearch(nums, num):
            if num > nums[-1]:
                return len(nums)
            if num < nums[0]:
                return 0
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) >> 1




        minNum, counts = [], []
        for num in nums:


