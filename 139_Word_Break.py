#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-2
#difficulty degree：
#problem: 139_Word_Break
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #用一个dp数组来存储可划分的下标，然后判断这些下标到当前下标之间的词是否在字典中
    def wordBreak(self, s, wordDict):
        d = {}
        for word in wordDict:
            d[word] = 1
        ls = len(s)
        dp = [-1]
        for i in range(ls):
            for index in dp:
                if s[index + 1: i + 1] in d:
                    dp.append(i)
                    break
        return dp[-1] == ls - 1



solute = Solution()
res = solute.wordBreak("leetcode", ["leet", "code"])

print(res)

