#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 278_First_Bad_Version.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            m = l + (r - l)//2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l