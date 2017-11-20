#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 8_string_to_integer_atoi
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def myAtoi(self, str):
		str_list = list(str)
		str_res = ""
		sign = 1
		index = 0
		res = 0
		for i in str_list:
			#先判断是否是空格，如果是且已经开始 数字的读取，则返回0
			if i == ' ':
				if index and str_res!= "":
					res = sign * int(str_res)
					return max(-2147483648, min(res,2147483647))
				continue
			# 判断是否是符号，如果是且已经开始 数字的读取，则返回0，否则开始 数字的读取，且存储符号位
			if i == '-' or i == '+':
				if index and str_res!= "":
					res = sign * int(str_res)
					return max(-2147483648, min(res,2147483647))
				if index:
					return 0
				index = 1
				sign = 1 if i == '+' else -1
				continue
			# 判断是否是数字，是则存储数据，否则开始 数字的读取
			if i.isdigit():
				index = 1
				str_res = str_res + i
				continue
			# 若出现除了数字，空格，符号以外的字符，则终止数字的读取
			else:
				if index and str_res!= "":
					res = sign * int(str_res)
					return max(-2147483648, min(res,2147483647))
				return 0
		#遍历结束，若没有返回值，则再进行一次判断
		res = sign * int(str_res)
		if index and str_res != "":
			return max(-2147483648, min(res,2147483647))
		return 0

str1 = "+0 123"
solute = Solution()
res = solute.myAtoi(str1)

print(res)