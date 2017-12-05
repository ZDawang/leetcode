#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 611_Valid_Triangle_Number.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #有两条边a,b 满足条件 c > abs(b - a) and c < a + b的都可以。
    #第一思路O(n2logn)
    #找任意两条边，剩下一条使用二分法查找
    def triangleNumber(self, nums):
        #寻找小于num的最后一个数的下标
        def BinarySearch(l, r, num):
            if nums[l] >= num: return l
            while l + 1 < r:
                m = (l + r)//2
                if nums[m] < num:
                    l = m
                else:
                    r = m - 1
            return r if nums[r] < num else l

        nums.sort()
        l, res = len(nums), 0
        for i in range(l):
            for j in range(i + 1, l):
                right = BinarySearch(j, l - 1, nums[i] + nums[j])
                res += right - j
        return res


    #O(N2)到O(n2logn)思路
    #二搜索起点不用从j开始，从上一个right开始就行了
    def triangleNumber3(self, nums):
        #寻找小于num的最后一个数的下标
        def BinarySearch(l, r, num):
            if nums[l] >= num: return l
            while l + 1 < r:
                m = (l + r)//2
                if nums[m] < num:
                    l = m
                else:
                    r = m - 1
            return r if nums[r] < num else l

        nums.sort()
        l, res = len(nums), 0
        for i in range(l):
            right = i + 1
            for j in range(i + 1, l):
                right = max(BinarySearch(right, l - 1, nums[i] + nums[j]), j)
                res += right - j
        return res



    #O(N2)思路
    #二搜索起点不用从j开始，从上一个right开始就行了
    #所以也不用二分法了。使用二分法会使复杂度在O(n2)到O(n2logn)
    def triangleNumber2(self, nums):
        nums.sort()
        l, res = len(nums), 0
        for i in range(l):
            maxIndex = i + 1
            for j in range(i + 1, l):
                while maxIndex < l and nums[maxIndex] < nums[i] + nums[j]:
                    maxIndex += 1
                if maxIndex > j:
                    res += (maxIndex - 1) - (j + 1) + 1
        return res


nums = [0,0,0]
solute = Solution()
res = solute.triangleNumber2(nums)