#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 65_Valid_Number.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False