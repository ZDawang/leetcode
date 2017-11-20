#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 316_Remove_Duplicate_Letters.py
#time_complecity:  
#space_complecity: 
#beats: 
import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        collect = collections.Counter(s)
        visited = {chr(x): False for x in range(97, 123)}
        minpos = 0
        res = []
        for c in s:
            collect[c] -= 1
            if visited[c] == True:
                continue
            #当前字符没出现在res中，且当前字符比res的最后一个小，
            #且res的最后一个字符在后面仍可以出现时，把res的最后一个字符删掉
            while(res and c < res[-1] and collect[res[-1]] != 0):
                visited[res.pop()] = False
            res.append(c)
            visited[c] = True
        return "".join(res)
            
        



s = "rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"
solute = Solution()
res = solute.removeDuplicateLetters(s)