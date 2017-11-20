#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 441_Arranging_Coins
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def arrangeCoins(self, n):
        i = 0
        while(i*i + i <= 2*n):
            i += 1
        return i
    def arrangeCoins2(self, n):
        return int(((8*n + 1)**0.5 - 1)//2)