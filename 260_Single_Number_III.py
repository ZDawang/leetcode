#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 260_Single_Number_III.py
#time_complecity:  
#space_complecity: 
#beats: 

from functools import reduce
class Solution(object):
    #首先得到两个数异或的结果，找到异或结果为1的那个比特位，说明两个数在这一位上不同。
    #根据这一位，将所有数分成两部分，两个数分别在这两部分中
    def singleNumber(self, nums):
        xorNum = reduce(lambda x, y: x ^ y, nums)
        diffBit = xorNum & (-xorNum)
        num1, num2 = 0, 0
        for num in nums:
            num1, num2 = (num1 ^ num, num2) if num & diffBit else (num1, num2 ^ num)
        return [num1, num2]

