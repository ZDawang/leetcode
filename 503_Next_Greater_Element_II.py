#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 503_Next_Greater_Element_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #栈，若一个数的下一个最大数不需要循环，则直接用栈即可。
    #就是把数字都放进栈里，如果它比栈顶的数大，则把栈顶的元素拿掉，栈顶的下个最大数就是当前数字。
    #最后栈里剩下的是一个递减的数列，此时，从头再遍历一遍。则会只剩一个最大数。达到cycle的目的。
    def nextGreaterElements(self, nums):
        stack = []
        greater = [0 for _ in range(len(nums))]
        #第一遍，找不需要cycle的。
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                greater[stack.pop()] = num
            stack.append(i)
        #寻找需要cycle的
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                greater[stack.pop()] = num
        #栈中剩下的最大数
        while stack:
            greater[stack.pop()] = -1
        return greater