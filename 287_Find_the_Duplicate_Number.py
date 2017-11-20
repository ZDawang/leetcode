#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 287_Find_the_Duplicate_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE,满足要求
    def findDuplicate1(self, nums):
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] == nums[j]:
                    return nums[i]

    #寻找数所在的区间，因为数最小为1，最大为l-1，如果比中间值也就是l/2小的数更多
    #那么我们要找的数就在中间值以下。 二分法+遍历，二分法不是对位置的二分，是对数值大小的二分
    #因为不涉及对mid值的判断，因此用二分法的第二种形式。
    def findDuplicate2(self, nums):
        l, r = 1, len(nums) - 1
        while(l < r):
            mid = l + (r - l)//2
            cnt = 0
            for num in nums:
                #此处为<=的原因是因为将m划到了l-mid之中
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return l

    #O(n)思想为若有重复数据，那么可以成一个环，首先找到环，然后找到环的入口，即重复数据
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        res = 0
        while 1:
            slow = nums[slow]
            res = nums[res]
            if slow == res:
                return res

nums = [1,1]
#nums = [2,5,1,1,4,3]
solute = Solution()
res = solute.findDuplicate(nums)
print(res)