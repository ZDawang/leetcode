#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 41_first_missing_positive
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #思路，本质是1到n的O(n)排序问题。
    #因为只需要找缺少的正数，所以我们只需要将1到l内的数按顺序放入到nums里面即可。如果缺失了某个正数，
    #那么对应位置上的数肯定不对，所以可以找到结果。
    def firstMissingPositive(self, nums):
        l = len(nums)
        for num in nums:
            #当数在1到l之间，且位置不对时，将num放入到正确位置。
            while num > 0 and num <= l and num != nums[num - 1]:
                nums[num - 1], num = num, nums[num - 1]
        for i in range(l):
            if nums[i] != i + 1:
                return i + 1
        return l + 1






nums = [3,4,-1,1]
solute = Solution()

res = solute.firstMissingPositive(nums)

print(res)