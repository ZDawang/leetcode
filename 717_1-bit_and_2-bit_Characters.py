#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 717_1-bit_and_2-bit_Characters.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #0,10,11是解码问题，而且是哈夫曼编码，所以bits的解码结果只有一种情况。
    #对它进行解码，看最后一位是不是0即可。
    def isOneBitCharacter(self, bits):
        if not bits or bits[-1] == 1: return False
        while i < len(bits) - 1:
            i = i + 2 if bits[i] == 1 else i + 1
        return i == len(bits) - 1
