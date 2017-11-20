#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 633_Sum_of_Square_Numbers.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(c ** 0.5)
        while left <= right:
            tmp = left ** 2 + right ** 2
            if tmp == c:
                return True
            elif tmp < c:
                left += 1
            else:
                right -= 1
        return False