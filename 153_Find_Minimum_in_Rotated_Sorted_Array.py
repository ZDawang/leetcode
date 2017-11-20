#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-
#difficulty degree：
#problem: 153_Find_Minimum_in_Rotated_Sorted_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(n)
    def findMin2(self, nums):
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] <= nums[i - 1]:
                return nums[i]

    #O(log(n))二分法
    def findMin3(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r)//2
            print(l, mid, r)
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[l]:
                r = mid
            else:
                return nums[l]


#两种二分法的区别：第一种l为+1，可以遍历所有，第二种没有对mid本身进行判断。
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while(l <= r):
            #对mid进行判断，以防错漏
            mid = l + (r-l)//2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

nums = [3,1,2]
solute = Solution()
res = solute.findMin(nums)
print(res)