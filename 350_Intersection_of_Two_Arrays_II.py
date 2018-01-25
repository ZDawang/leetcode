#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 350_Intersection_of_Two_Arrays_II.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import Counter
class Solution(object):
    #统计两个数组中的数字出现次数。然后取出现的最小次数。
    def intersect(self, nums1, nums2):
        counts1, counts2 = Counter(nums1), Counter(nums2)
        res = []
        for num in counts1:
            if not num in counts2:
                continue
            res += [num] * min(counts1[num], counts2[num])
        return res