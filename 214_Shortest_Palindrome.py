#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-26
#difficulty degree：
#problem: 214_Shortest_Palindrome
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def shortestPalindrome(self, s):
        if not s: return ""
        l = len(s)
        mid = l // 2
        for m in range(mid, -1, -1):
            #奇数长度的回文
            if s[:m] == s[m + 1: 2*m + 1][::-1]:
                return s[2*m + 1:][::-1] + s
            #偶数长度
            if s[:m] == s[m: 2*m][::-1]:
                return s[2*m:][::-1] + s

    #KMP算法
    #得到的最终结果是reverse_s的后缀与s的前缀相同的长度,也就是s的前k个字母与reverse_s的后k个字母相同，也就是回文
    def shortestPalindrome(self, s):
        S = s + "#" + s[::-1]
        l = len(S)
        table = [0] * len(S)
        #跳转表的构建
        for i in range(1, l):
            #找出i-1位的跳转位置
            index = table[i - 1]
            #若i位与i-1位跳转位置的后一个字符不同，则寻找i-1跳转位置的前一个跳转位置。
            #本质就是先找最长前缀的位置，不行的话，就找短一点的相同前缀的位置。
            while index > 0 and S[index] != S[i]:
                index = table[index - 1]

            table[i] = index + 1 if S[index] == S[i] else 0
        return s[table[-1]:][::-1] + s

def getnext(S):
    l = len(S)
    table = [0] * len(S)
    for i in range(1, l):
        #找出i-1位的跳转位置
        index = table[i - 1]
        #若i位与i-1位跳转位置的后一个字符不同，则寻找i-1跳转位置的前一个跳转位置。
        #本质就是先找最长前缀的位置，不行的话，就找短一点的相同前缀的位置。
        while index > 0 and S[index] != S[i]:
            index = table[index - 1]

        table[i] = index + 1 if S[index] == S[i] else 0
    return table


s = "abcdefghijklmnabcd"
solute = Solution()
#res = solute.shortestPalindrome(s)
table = getnext(s)