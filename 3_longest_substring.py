#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#date:2017-3-7
#difficulty degree ：medium
#problem:3. Longest Substring Without Repeating Characters
#time_complecity:  
#space_complecity: 
#beats: 

#使用一个中间字符串变量来遍历字符串，若发现字母已出现，则初始化中间字符串变量

class Solution(object):
    #tmp存储到当前字符没有重复字符的子串。
    #时间复杂度O(n)到O(n2)
    def lengthOfLongestSubstring(self, s):
        res, tmp = 0, ""
        for c in s:
            #从重复的那个字母下一个字母开始截取
            tmp = tmp[tmp.find(c) + 1:] + c
            res = max(res, len(tmp))
        return res

    #使用d来存储字符的最后出现的位置，这样就不用再在字符串中寻找了
    #O(n)
    #这样tmp存储到当前字符的最长子串长度就行了
    def lengthOfLongestSubstring2(self, s):
        d = {}
        res, tmp = 0, 0
        for i, c in enumerate(s):
            pre = d.get(c, -1)
            d[c] = i
            #tmp+1是子串中没有出现当前字符的长度
            #i-pre时如果出现的话，从前一个位置pre+1,到当前位置i的长度
            tmp = min(tmp + 1, i - pre)
            res = max(res, tmp)
        return res
            




solute = Solution()
s = "abcabcbb"

res = solute.lengthOfLongestSubstring(s)
print(res)