#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isPowerOfFour(self, num):
        return num & (num - 1) == 0 and (num - 1) % 3 == 0