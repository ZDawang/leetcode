#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-26
#difficulty degree：
#problem: 151_Reverse_Words_in_a_String
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])