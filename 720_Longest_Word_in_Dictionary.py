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
    #BFS
    def longestWord(self, words):
        wordSet = set(words)
        queue = [word for word in words if len(word) == 1]
        res = min(queue)
        while queue:
            word = queue.pop(0)
            for c in "abcdefghijklmnopqrstuvwxyz":
                if word + c in wordSet:
                    newword = word + c
                    queue.append(newword)
                    res = res if len(res) > len(newword) or (len(res) == len(newword) and res < newword) else newword
        return res

    