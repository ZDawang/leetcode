#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-30
#difficulty degree：
#problem: 628_Maximum_Product_of_Three_Numbers
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #寻找最小的两个数以及最大的三个数
    def maximumProduct(self, nums):
        minnum = min(nums)
        maxnum = max(nums)
        maxnums = [minnum, minnum, minnum]
        minnums = [maxnum, maxnum]
        for num in nums:
            if num > min(maxnums):
                maxnums.remove(min(maxnums))
                maxnums.append(num)
            if num < max(minnums):
                minnums.remove(max(minnums))
                minnums.append(num)
        res1 = maxnums[0] * maxnums[1] * maxnums[2]
        res2 = minnums[0] * minnums[1] * max(maxnums)
        return res1 if res1 > res2 else res2

nums = [1,2,3,2]
solute = Solution()
res = solute.maximumProduct(nums)  
