#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3- 8
#difficulty degree：
#problem: 9_palindrome_number
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def isPalindrome(self, x):
		# 除了将数分成左右两边以外的方法： 先计算数的长度，然后最高位与最低位比较，不一样则F，一样则继续
		if x < 0:
			return False
		div = x
		len_x = 0
		while(div>0):
			div = div//10
			len_x =len_x + 1
		for i in range((len_x)//2):
			print(x//(10**(len_x - i -1))-x//(10**(len_x -i))*10, (x%(10**(i+1)))//(10**i))
			if (x//(10**(len_x - i -1))-x//(10**(len_x -i))*10) != (x%(10**(i+1)))//(10**i):
				return False
		return True

class Solution2(object):
	def isPalindrome(self, x):
		if x < 0:
			return False
		rev = 0
		while(x>rev):
			rev = rev * 10 + x%10
			x = x//10
		return(x == rev or x == rev/10)

x = 545545
solute = Solution2()
res = solute.isPalindrome(x)

print(res)
