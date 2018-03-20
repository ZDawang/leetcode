#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 47_Permutations_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def permuteUnique(self, nums):
        def recurse(d, res, l):
            if -1 in d.values():
                return
            if sum(d.values()) == 0:
                res.append(l)
                return
            for d_element in d:
                temp = d.copy()
                temp[d_element] -= 1
                recurse(temp, res, l + [d_element])
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = []
        recurse(d, res, [])
        return res

