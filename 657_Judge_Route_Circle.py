#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 657_Judge_Route_Circle
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def judgeCircle(self, moves):
        return moves.count("D") == moves.count("U") and moves.count("L") == moves.count("R")