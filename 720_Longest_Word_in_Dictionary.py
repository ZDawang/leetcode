#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 720_Longest_Word_in_Dictionary.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路，标准BFS，只击败了百分之37
    def longestWord(self, words):
        wordSet = set(words)
        queue = [""]
        res = ""
        while queue:
            word = queue.pop(0)
            for c in "abcdefghijklmnopqrstuvwxyz":
                newword = word + c
                if newword in wordSet:
                    queue.append(newword)
                    res = res if len(res) > len(newword) or (len(res) == len(newword) and res < newword) else newword
        return res

    #在答案里看到的一种方法，找到一个比当前结果长的，再看当前字符能够从words里构成
    #击败百分之97
    def longestWord2(self, words):
        wordSet = set(words)
        res = ""
        for word in wordSet:
            #若当前word比res短，跳过
            if len(word) < len(res) or (len(word) == len(res) and word < res):
                continue
            #查看当前word是否能从单个字符推到
            for i in range(1, len(word) + 1):
                if not word[:i] in wordSet:
                    break
            #若可以，更新res
            res = word if i == len(word) else res
        return res
