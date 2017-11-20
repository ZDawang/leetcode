#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-12
#difficulty degree：
#problem: 89_gray_code
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def grayCode(self, n):
        res = [0]
        for i in range(n):
            res += [x + 2**i for x in reversed(res)]
        return results