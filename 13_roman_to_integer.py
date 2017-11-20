#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 13_roman_to_integer
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def romanToInt(self, s):
		res = 0
		roman_dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
		for i in range(len(s) - 1):
			if roman_dic[s[i]] < roman_dic[s[i+1]]:
				res = res - roman_dic[s[i]]
			else:
				res = res + roman_dic[s[i]]
		return res + roman_dic[s[-1]]

s = "DCLIV"

solute = Solution()

res = solute.romanToInt(s)
print(res)