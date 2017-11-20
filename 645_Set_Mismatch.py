#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用哈希找出重复数字，然后使用n *(n + 1)/2 - (sum(nums) - dupNum)求出缺失数字
    #时间O(n),空间O(n)
    def findErrorNums(self, nums):
        d = set()
        n, dupNum = len(nums), 0
        for num in nums:
            if num in d:
                dupNum = num
                break
            d.add(num)
        return [dupNum, n *(n + 1)/2 + dupNum - sum(nums)]

    #优化为空间O(1)
    #思路，与442题类似: 若有两个数相同，则指向的下标一致。
    #可先把遍历过的数作为下标对应的数变为负数，若检测到当前数作为下标对应的数是负数时
    #则说明这个下标已经遍历过，即这个数是重复的数。
    #因为数是从1到n，下标是0到n-1，所以下标应选abs(num)-1
    def findErrorNums(self, nums):
        sums = sum(nums)
        for num in nums:
            if nums[num - 1] < 0:
                dupNum = num
                break
            else:
                nums[num - 1] *= -1
        return [dupNum, n * (n + 1)/2 + dupNum - sum(nums)]
