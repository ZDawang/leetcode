#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 88_merge_sorted_array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        loc = 0
        l = m
        for num in nums2:
            while nums1[loc] <= num and loc < l:
                loc += 1
            nums1.insert(loc, num)
            loc += 1
            l += 1
        l = len(nums1)
        while l > m + n:
            nums1.pop()
            l -= 1

nums1 = [0]
nums2 = [9]

solute = Solution()
solute.merge(nums1, 0, nums2, 1)
print(nums1)