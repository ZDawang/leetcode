#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #贪心
    #计算能种的最多花有多少。
    def canPlaceFlowers(self, flowerbed, n):
        canplace = True
        res = 0
        for f in flowerbed:
            if f == 1:
                if canplace == False:
                    res -= 1
                canplace = False
            else:
                res = res + 1 if canplace else res
                canplace = not canplace
        return True if res >= n else False