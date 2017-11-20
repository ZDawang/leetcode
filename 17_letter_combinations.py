#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-13
#difficulty degree：
#problem: 17_letter_combinations
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def letterCombinations(self, digits):
		butt = [" ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		res = [""]
		if len(digits) == 0:
			return []
		for i in digits:
			if int(i) == 1:
				continue
			elif int(i) == 0:
				for j in res:
					j = j + butt[0]
			else:
				temp_len = len(res)
				res = len(butt[int(i)-1])*res
				for j in range(len(res)):
					res[j] = res[j] + butt[int(i)-1][j//temp_len]
		return res
digits = "0"
solute = Solution()
res = solute.letterCombinations(digits)

print(res)