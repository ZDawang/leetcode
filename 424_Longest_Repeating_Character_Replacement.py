#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 424_Longest_Repeating_Character_Replacement.py
#time_complecity:  
#space_complecity: 
#beats: 
import collections
class Solution(object):
    #滑动窗
    def characterReplacement(self, s, k):
        #存储字母出现的次数
        count = [0] * 26
        res, i, j = 0, 0, 0
        for j in range(len(s)):
            count[ord(s[j]) - 65] += 1
            #找到次数最多的字符
            max_count = max(count)
            while j - i + 1 - max_count > k:
                count[ord(s[i]) - 65] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res

s = "AABABBA"
solute = Solution()
res = solute.characterReplacement(s, 1)

    
