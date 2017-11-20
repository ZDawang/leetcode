#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 374_Guess_Number_Higher_or_Lower.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n
        while l < r:
            m = l + (r - l)//2
            if guess(m) == 1:
                l = m + 1
            else:
                r = m
        return l