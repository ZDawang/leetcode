#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3- 8
#difficulty degree：medium
#problem: 5_longest_palindromic_substring
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def longestPalindrome(self, s):
		res_len = 0
		res = ""
		l1 = len(s)
		for i in range(1, l1):
			#寻找奇数长度的回文子串
			for k_odd in range(1, min(i+ 1, l1 - i)):
				#若找到长度大于最大长度的回文子串，更新，同时，若仍可以继续下去，则继续循环
				if (s[i - k_odd] == s[i + k_odd]):
					if k_odd+k_odd+1 > res_len:
						res_len = k_odd+k_odd+1
						res = s[i-k_odd : i+k_odd+1]
					continue
				else:
				#若找到长度大于最大长度的回文子串，更新，若已到当前子串的最大长度，跳出循环
					if k_odd+k_odd-1 > res_len:
						res_len = k_odd+k_odd-1
						res = s[i-k_odd+1 : i+k_odd]
					break
			#寻找偶数长度的回文子串，思路同奇数
			for k_even in range(1, min(i, l1 - i) + 1):
				print(k_even,min(i, l1 - i))
				if (s[i-k_even] == s[i+k_even-1]):
					if k_even+k_even >res_len:
						res_len = k_even + k_even
						res = s[i-k_even : i+k_even]
					continue
				else:
					if k_even+k_even -2 >res_len:
						res_len = k_even + k_even -2
						res = s[i-k_even + 1: i+k_even -1]
					break
			print (res_len)
			if i >= l1 - (res_len+1)//2:
				return res


s = "abcda"
solute = Solution()
res = solute.longestPalindrome(s)
print(res)