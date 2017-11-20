#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 318_Maximum_Product_of_Word_Lengths.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用set来保存每个word的字母
    def maxProduct(self, words):
        l = len(words)
        wordset = [0] * l
        for i in range(l):
            wordset[i] = set(word[i])
        res = 0
        for i in range(l):
            for j in range(i):
                if not wordset[i] & wordset[j]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

    #使用一个26位的数来存储每个word的set
    def maxProduct(self, words):
        d = {}
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - 97
            d[mask] = max(d.get(mask, 0), len(word))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
        