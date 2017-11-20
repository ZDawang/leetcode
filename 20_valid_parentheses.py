#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 20_valid_parentheses
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def isValid(self, s):
		stack = []
		d={'(':')', '[':']', '{':'}'}
		for st in s:
			if st in d:
				stack.append(st)
			else:
				if stack and d[stack.pop()] == st:
					continue
				else:
					return False
		return True if not stack else False

s = ""

solute = Solution()
res = solute.isValid(s)

print(res)