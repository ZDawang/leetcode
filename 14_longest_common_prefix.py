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


    #首先找到最短的那个字符串作为公共前缀，然后不断寻找最小的公共前缀
    def longestCommonPrefix2(self, strs):
        if not strs: return ""
        res = min(strs, key = lambda x: len(x))
        end = len(res)
        for s in strs:
            #寻找公共前缀
            for i in range(min(end, len(s))):
                if s[i] != res[i]:
                    end = i
                    break
        return res[:end]


strs = ["aaa", "aa", "aaa"]
solute = Solution()
res = solute.longestCommonPrefix(strs)

print(res)