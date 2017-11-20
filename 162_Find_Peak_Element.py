#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 162_Find_Peak_Element
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #二分查找
    def findPeakElement(self, nums):

        def find(nums, l, r, res):
            if l > r:
                return False
            mid = l + (r - l)//2
            print(l, mid, r)
            if nums[mid] > nums[mid - 1]  and nums[mid] > nums[mid + 1]:
                print(mid)
                res[0] = mid
                return True
            if find(nums, mid + 1, r, res):return True
            if find(nums, l, mid - 1, res):return True
            return False

        len_nums = len(nums)
        if len_nums <= 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len_nums - 1
        l, r = 0, len(nums)-1
        res = [0]
        find(nums, l, r, res)
        return res[0]

nums = [3,4,3,2,1]
solute = Solution()
res = solute.findPeakElement(nums)
print(res)