#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 334_Increasing_Triplet_Subsequence.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路：DP。
    #使用两个数组，分别存储到当前数字，递增长度为1的最小值。递增长度为2的第二个数的最小值。
    #再进行空间复杂度的优化为O(1)即可。
    def increasingTriplet(self, nums):
        min1, min2 = float("inf"), float("inf")
        for num in nums:
            if num > min2:
                return True
            #更新min2的值
            if num > min1:
                min2 = min(min2, num)
            #更新min1的值
            min1 = min(num, min1)
        return False

