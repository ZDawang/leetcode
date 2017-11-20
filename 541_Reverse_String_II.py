#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-27
#difficulty degree：
#problem: 541_Reverse_String_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def reverseStr(self, s, k):
        l = len(s)
        i = 0
        while(i < l):
            s = s[:i] + s[i: i + k][::-1] + s[i + k:]
            i += 2 * k
        return s