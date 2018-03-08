#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 784_Letter_Case_Permutation.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dfs,若碰到字母，则大小写分别dfs，若为数字，直接向下DFS
    def letterCasePermutation(self, S):
        def dfs(i, tmp):
            if i == n:
                res.append(tmp)
                return
            if S[i].isalpha():
                dfs(i + 1, tmp + S[i].lower())
                dfs(i + 1, tmp + S[i].upper())
            else:
                dfs(i + 1, tmp + S[i])

        res = []
        n = len(S)
        dfs(0, "")
        return res