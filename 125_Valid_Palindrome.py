#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 125_Valid_Palindrome
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def isPalindrome(self, s):
        lows = ""
        for c in s:
            if c.isalnum(): lows += c.lower()
        return lows == lows[::-1]

    def isPalindrome2(self, s):
        l = len(s)
        i, j = 0, l - 1
        while(i < j):
            while(not s[i].isalnum() and i < l - 1):
                i += 1
            while(not s[j].isalnum() and j > 0):
                j -= 1
            if s[i].lower() != s[j].lower():
                if i == l - 1 and j == 0:
                    return True
                return False
            i += 1
            j -= 1
        return True
