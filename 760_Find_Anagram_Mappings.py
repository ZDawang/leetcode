#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 760_Find_Anagram_Mappings
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #哈希表
    def anagramMappings(self, A, B):
        loc = {num: i for i, num in enumerate(B)}
        P = [0] * len(A)
        for i, num in enumerate(A):
            P[i] = loc[num]
        return P