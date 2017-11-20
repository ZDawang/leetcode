#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-16
#difficulty degree：
#problem: 229_Majority_Element_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #摩尔投票法
    def majorityElement(self, nums):
        if not nums:
            return []
        n1, n2, c1, c2 = 0, 1, 0, 0
        for n in nums:
            if n == n1:
                c1 += 1
                continue
            if n == n2:
                c2 += 1
                continue
            if c1 == 0:
                n1 = n
                c1 = 1
                continue
            if c2 == 0:
                n2 = n
                c2 = 1
                continue
            c1 -= 1
            c2 -= 1
        return [n for n in [n1, n2] if nums.count(n) > len(nums)//3]