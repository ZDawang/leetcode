#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 31_next_permutation
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #从后向前，比较数与后一个数的大小，若后面的数比较大，则可提到前面，后面的数再进行排序
    def nextPermutation(self, nums):
        l = len(nums)
        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                diff = 10000
                index = 0
                little_bigger = 0
                for j in range(i + 1, l):
                    if 0 < nums[j] - nums[i] < diff:
                        little_bigger = nums[j]
                        diff = nums[j] - nums[i]
                        index = j
                nums[index] = nums[i]
                nums[i] = little_bigger
                a = sorted(nums[i + 1:])
                for k in range(i + 1,l):
                    nums[k] = a[k - i - 1]
                return
        nums.sort()
        return

nums = [1,2]
solute = Solution()
solute.nextPermutation(nums)

print(nums)
