#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #因为想要结果最大，因为分母是第一个数字，则分子要尽可能的小。
    #因为所有的数字都大于1，所以把后面的数字挨个相除就是最小的分子。
    def optimalDivision(self, nums):
        A = map(str, nums)
        if len(A) <= 2:
            return '/'.join(A)
        return A[0] + '/(' + '/'.join(A[1:]) + ')'
