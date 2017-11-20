#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 680_Valid_Palindrome_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def validPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s[i + 1: j + 1]) or self.isPalindrome(s[i: j])
            i += 1
            j -= 1
        return True

    def isPalindrome(self, s):
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l - 1 - i]:
                return False
        return True


