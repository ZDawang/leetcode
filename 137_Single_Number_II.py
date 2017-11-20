#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 137_Single_Number_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用x2，x1，作为每一比特位的计数器，出现3次则清0
    def singleNumber(self, nums):
        x2, x1, mask = 0, 0, 0
        for num in nums:
            #x1&inum 统计x1中的哪些位需要进位，x2^(x1 & num)则进行进位
            x2 = x2 ^ (x1 & num)
            #x1的计数
            x1 = x1 ^ num
            #统计哪些位到了3个，也就是x2x1 = 11
            mask = ~(x2 & x1)
            #清零
            x2 = mask & x2
            x1 = mask & x1
        #因为重复3次，所以x1，x2在只重复1次的那个数对应的比特位都是1
        return x1


