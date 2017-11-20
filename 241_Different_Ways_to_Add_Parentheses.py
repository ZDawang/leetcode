#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 241_Different_Ways_to_Add_Parentheses.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dfs+memo
    #对于一个字符串比如2*3-4*5,可以分成[2]*[3-4*5],[2*3]-[4*5],[2*3-4]*[5]来遍历计算出所有的结果
    #使用memo存储已经计算过的str
    #所以对整个字符串不断遍历，得到所有结果。
    def diffWaysToCompute(self, input):
        def dfs(s):
            if s in d: return d[s]
            if s.isdigit(): return [int(s)]
            res = []
            for i in range(len(s)):
                if s[i] == "*":
                    res += [x * y for x in dfs(s[:i]) for y in dfs(s[i+1:])]
                elif s[i] == "-":
                    res += [x - y for x in dfs(s[:i]) for y in dfs(s[i+1:])]
                elif s[i] == "+":
                    res += [x + y for x in dfs(s[:i]) for y in dfs(s[i+1:])]
            d[s] = res
            return res
        d = {}
        return dfs(input)

input = "2*3-4*5"
solute = Solution()
res = solute.diffWaysToCompute(input)