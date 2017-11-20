#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 167_Two_Sum_II_Input_array_is_sorted
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while(l <= r):
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1