#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-26
#difficulty degree：
#problem: 522_Longest_Uncommon_Subsequence_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findLUSlength(self, strs):
        def subseq(w1, w2):
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)

        strs.sort(key = len, reverse = True)
        l = len(strs)
        for i in range(l):
            index = 0
            for j in range(l):
                if i == j:
                    continue
                if subseq(strs[i], strs[j]):
                    index = 1
                    break
            if index == 0:
                return len(strs[i])
        return -1