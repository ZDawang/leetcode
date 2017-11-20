#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 594_Longest_Harmonious_Subsequence
#time_complecity:  
#space_complecity: 
#beats: 

import collections
class Solution(object):
    def findLHS(self, nums):
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        res = 0
        for key in d:
            if key - 1 in d:
                res = max(res, d[key] + d[key - 1])
        return res