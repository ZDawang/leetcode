#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 744_Find_Smallest_Letter_Greater_Than_Target
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #二分
    def nextGreatestLetter(self, letters, target):
        if not letters: return ""
        if target > letters[-1]: return letters[0]
        l, r = 0, len(letters) - 1
        while l < r:
            m = l + (r - l)//2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
        return letters[l]