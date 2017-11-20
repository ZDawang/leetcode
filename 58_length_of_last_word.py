#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 58_length_of_last_word
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def lengthOfLastWord(self, s):
        i, index = 0, 0
        for k in reversed(s):
            if k ==" ":
                if index == 1:
                    return i
            else:
                index = 1
                i += 1
        return i

s = "aaaa"
solute = Solution()
res = solute.lengthOfLastWord(s)

print(res)