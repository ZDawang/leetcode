#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 526_Beautiful_Arrangement.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dfs + memo, 使用visit来表示数有没有使用过
    def countArrangement(self, N):
        def dfs(visit, index):
            if index == N + 1: return 1
            if visit in memo: return memo[visit]
            res = 0
            for i in range(1, N + 1):
                num = 1 << (i - 1)
                if num & visit and (i % index == 0 or index % i == 0):
                    res += dfs(visit ^ num, index + 1)
            memo[visit] = res
            return res

        memo = {}
        return dfs(2 ** N - 1, 1)