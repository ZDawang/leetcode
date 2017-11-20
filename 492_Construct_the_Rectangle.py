#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 492_Construct_the_Rectangle.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def constructRectangle(self, area):
        x = int(area ** 0.5)
        while area % x != 0: x -= 1
        return [area/x, x]