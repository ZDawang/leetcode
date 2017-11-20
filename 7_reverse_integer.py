#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-8
#difficulty degree：
#problem: 7_reverse_integer
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def reverse(self, x):
		sign = 1

		if(x)<0:
			sign = -1
		str_num = str(abs(x))
		str_rev_num = int(str_num[::-1])

		res = str_rev_num * sign
		if -2147483648 <= res <= 2147483647:
			return res
		return 0


x = 
solute = Solution()
res = solute.reverse(x)
print(res)