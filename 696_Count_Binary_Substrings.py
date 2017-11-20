#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 696_Count_Binary_Substrings.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #统计前一个连续相同的个数，再做运算。
    #比如前面有3个连续，现在有5个连续，那么总共应该有min(3,5)种可能
    def countBinarySubstrings(self, s):
        tmp, repeat = 1, []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tmp += 1
            else:
                repeat.append(tmp)
                tmp = 1
        repeat.append(tmp)
        return sum([min(repeat[i], repeat[i - 1]) for i in range(1, len(repeat))])

    #优化为O（1）
    def countBinarySubstrings2(self, s):
        res = 0
        pre, cur = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(pre, cur)
                pre, cur = cur, 1
        return res + min(pre, cur)



