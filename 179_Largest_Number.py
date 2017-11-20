#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 179_Largest_Number.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #排序的高级用法
    def largestNumber(self, nums):
        strNums = [str(num) for num in nums]
        compare = lambda x, y: 1 if x + y > y + x else -1
        strNums.sort(cmp = compare)
        return "".join(strNums).lstrip("0") or "0"
