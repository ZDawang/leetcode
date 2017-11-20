#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 581_Shortest_Unsorted_Continuous_Subarray
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #从前往后，找到不是递增的数作为end， 从后向前，找到不是递减的一段作为start
    def findUnsortedSubarray(self, nums):
        l = len(nums)
        start, end = 0, -1
        min_num, max_num = nums[-1], nums[0]
        for i in range(l):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[l - 1 - i])
            if nums[i] < max_num: end = i
            if nums[l - 1 - i] > min_num: start = l - 1 - i
        return end - start + 1


    def findUnsortedSubarray2(self, nums):
        if not nums: return 0
        minnum, maxnum = nums[-1], nums[0]
        left, right = 0, -1
        #从前向后，找到需要调整的右边界
        #寻找方法为，若当前数比当前的最大数小，则说明这个数的位置肯定不对，就把它作为右边界
        for i in range(len(nums)):
            if nums[i] < maxnum:
                right = i
            else:
                maxnum = nums[i]
        #从后向前，找到需要调整的左边界
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > minnum:
                left = i
            else:
                minnum = nums[i]
        return right - left + 1


nums = [2,3,3,2]
solute = Solution()
res = solute.findUnsortedSubarray(nums)
