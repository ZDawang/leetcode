#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 477_Total_Hamming_Distance.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #统计每一个bit位的0的个数。
    #设有m个1，n个0，则这一bit位的汉明距离为：
    #对于1来说，有m*n，对于0来说，有n*m。
    #因为有重复，所以汉明距离为 (m*n+m*n)/2=m*n
    def totalHammingDistance(self, nums):
        count = [0] * 32
        for num in nums:
            mask = 1
            for i in range(32):
                if mask & num:
                    count[i] += 1
                mask = mask << 1
        return sum(c * (len(nums) - c) for c in count)

    def totalHammingDistance2(self, nums):
        mask, res, n = 1, 0, len(nums)
        for i in range(32):
            count = 0
            for num in nums:
                if mask & num:
                    count += 1
            res += count * (n - count)
            mask = mask << 1
        return res