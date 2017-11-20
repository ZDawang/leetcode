#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-17
#difficulty degree：
#problem: 187_Repeated_DNA_Sequences
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        d = {}
        res = []
        for i in range(len(s) - 9):
            str1 = s[i: i + 10]
            d[str1] = d.setdefault(str1, 0) + 1
            if d[str1] == 2:
                res.append(str1)
        return res

s = "AAAAAAAAAAA"
solute = Solution()
res = solute.findRepeatedDnaSequences(s)
print(res)