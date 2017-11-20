#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 423_Reconstruct_Original_Digits_from_English
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def originalDigits(self, s):
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        count = {}
        count[0] = d.get("z", 0)
        count[2] = d.get("w", 0)
        count[4] = d.get("u", 0)
        count[6] = d.get("x", 0)
        count[8] = d.get("g", 0)
        count[3] = d.get("h", 0) - count[8]
        count[5] = d.get("f", 0) - count[4]
        count[7] = d.get("v", 0) - count[5]
        count[1] = d.get("o", 0) - count[0] - count[2] - count[4]
        count[9] = d.get("i", 0) - count[5] - count[6] - count[8]
        res = ""
        for i in range(10):
            res += str(i) * count[i]
        return res


