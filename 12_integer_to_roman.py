#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 12_integer_to_roman
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def intToRoman(self, num):
		#
		res = ""

		table_num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
		str_num = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

		for i in range(len(table_num)):
			while(num >= table_num[i]):
				res = res + str_num[i]
				num = num - table_num[i]
		return res


class Solution2(object):
	#将十进制数字的每一位分别对应到表中
	def intToRoman(self, num):
		str_num =["","I","II","III","IV","V","VI","VII","VIII","IX",
					"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC",
					"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM",
					"","M","MM","MMM","MMMM"]
		return str_num[num//1000+30]+str_num[(num//100)%10+20]+str_num[(num//10)%10+10]+str_num[num%10];

num = 654
solute = Solution2()
res = solute.intToRoman(num)
print(res)
