#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-21
#difficulty degree：
#problem: 22_generate_parentheses
#time_complecity:  
#space_complecity: 
#beats: 

class Solution2(object):
	def generateParenthesis(self, n):
		def gen(right, left, res, string):
			if left > right:
				return
			if right == left == 0:
				res.append(string)
				return
			if left:
				gen(right, left-1, res, string + '(')
			if right:
				gen(right-1, left, res, string + ')')

        res = []
		gen(n, n, res, "")
		return res




solute = Solution()
res = solute.generateParenthesis(3)
print(res)