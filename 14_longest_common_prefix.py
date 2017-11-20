#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 14_longest_common_prefix
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
	def longestCommonPrefix(self, strs):
		if strs == []:
			return ""
		res = strs[0]
		len_res = len(res)
		for str1 in strs:
			for i in range(min(len_res, len(str1))):
				if res[i] != str1[i]:
					res = res[:i]
					len_res = i
					break
			(res, len_res) = (res, len_res) if len(str1)>len_res else (str1, len(str1))
		return res 

strs = ["aaa", "aa", "aaa"]
solute = Solution()
res = solute.longestCommonPrefix(strs)

print(res)