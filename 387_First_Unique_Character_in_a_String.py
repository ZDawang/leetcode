#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 387_First_Unique_Character_in_a_String.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def firstUniqChar(self, s):
        #若是只出现过一次，存储字母下标，出现过多次为0，没出现过为-1
        visit = [-1] * 26
        for i in range(len(s)):
            index = ord(s[i]) - 97
            if visit[index] >= 0:
                visit[index] = 0
            else:
                visit[index] = i + 1
        once = [x for x in visit if x > 0]
        return min(once) - 1 if once else -1