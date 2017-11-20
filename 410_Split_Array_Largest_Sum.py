#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-5
#difficulty degree：
#problem: 410_Split_Array_Largest_Sum
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #看思路，结果的最小值为max(nums)，最大值为sum(nums)，所以在这个区间进行二分法搜索
    def splitArray(self, nums, m):
        l, r = max(nums), sum(nums)
        while(l < r):
            mid = l + (r - l) // 2
            if not self.splitable(nums, mid, m):
                l = mid + 1
            else:
                r = mid
        return l

    def splitable(self, nums, m, cut):
        sums = 0
        i = 0
        l = len(nums)
        for num in nums:
            if sums + num <= m:
                sums = sums + num
            else:
                sums = num
                cut -= 1
        return cut > 0

solute = Solution()
res = solute.splitArray([7,2,5,10,8], 2)
print(res)




