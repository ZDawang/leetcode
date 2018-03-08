#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 771_Jewels_and_Stones.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def numJewelsInStones(self, J, S):
        d = set(J)
        return sum(1 for c in S if c in d)