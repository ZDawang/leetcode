#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 673_Number_of_Longest_Increasing_Subsequence.py
#time_complecity:  
#space_complecity: 
#beats: 
from collections import defaultdict
class Solution(object):
    #DP
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

    #O(nlogn)DP思路，与300题一样。
    #minNum[i]表示 长度为i的递增子串 的结尾最小数字。
    #count[i][num] 表示长度为i的递增子串的结尾为num的子串数量。
    #size记录最长的子串长度。
    def findNumberOfLIS2(self, nums):
        #二分搜索，在nums中找到插入的位置。
        def binarySearch(nums, num):
            if not nums or num > nums[-1]:
                return len(nums)
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) >> 1
                if nums[m] < num:
                    l = m + 1
                else:
                    r = m
            return l

        if not nums: return 0
        minNum, counts = [float("inf")] * len(nums), [defaultdict(int) for _ in range(len(nums))]
        size = 0
        for num in nums:
            #获取插入位置，也就是当前数字作为最后一个数字的 最长子串长度。
            index = binarySearch(minNum, num)
            #更新minNum与size
            minNum[index] = num
            size = max(size, index)
            #更新counts,将counts[index-1]中值小于num的次数的和，加入到counts[index][num]中
            if index == 0:
                counts[index][num] += 1
            else:
                counts[index][num] += sum(v for k, v in counts[index - 1].items() if k < num)
        return sum(counts[size].values())


nums = [1,3,5,4,7]
solute = Solution()
res = solute.findNumberOfLIS2(nums)