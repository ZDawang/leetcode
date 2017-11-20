#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def palindromePairs(self, words):
        def ispalindrome(s):
            return s == s[::-1]
        d = {}
        for i in range(len(words)):
            d[words[i]] = i
        valid_pals = []
        for word, k in d.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if ispalindrome(pref): 
                    back = suf[::-1]
                    if back != word and back in d:
                        valid_pals.append([d[back],  k])
                if j != n and ispalindrome(suf):
                    back = pref[::-1]
                    if back != word and back in d:
                        valid_pals.append([k, d[back]])
        return valid_pals
