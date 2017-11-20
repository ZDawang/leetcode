#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 566_Reshape_the_Matrix
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def matrixReshape(self, nums, r, c):
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        one_dimen_nums = []
        for i in range(m):
            one_dimen_nums += nums[i]

        if r == 1:
            return one_dimen_nums
        new_nums = []
        for i in range(r):
            new_nums += [one_dimen_nums[c * i: c * (i + 1)]]
        return new_nums