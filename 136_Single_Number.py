#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 136_Single_Number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路：将数作为下标，那么只有单次出现的为负数，结果发现要求只是整数，没有负数，方法不行

    #hash
    def singleNumber(self, nums):
        d = {}
        for num in nums:
            d[num] = d.setdefault(num, 0) + 1

        for key in d:
            if d[key] == 1:
                return key

    #O(1)方法：需要在原数组上做操作，将数加一个小数？可行
    #亦或
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
