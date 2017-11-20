#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 275_H-Index_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def hIndex(self, citations):
        length = len(citations)
        #当没有文献或者所有文献被引用数都为0时
        if length == 0 or citations[-1] == 0: return 0
        l, r = 0, length - 1
        while l < r:
            m = (l + r)//2
            #要寻找的数是最小的i，使citations[i] >= len(citations) - i
            #也就是被引用数 大于等于 文献数的最大值。
            if citations[m] < length - m:
                l = m + 1
            else:
                r = m
        return length - l