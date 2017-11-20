#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 496_Next_Greater_Element_I.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #对于一个数，找到比它大的数以后 就把它移除栈
    def nextGreaterElement(self, findNums, nums):
        d, stack = {}, []
        for num in nums:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
        res = []
        for num in findNums:
            res.append(d.get(num, -1))
        return res

