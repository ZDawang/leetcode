#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 52_N-Queens_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def totalNQueens(self, n):
        def dfs(solute, diff_d, sum_d, n):
            x = len(solute)
            if x == n: return 1
            count = 0
            for y in range(n):
                if (y in solute) or (x + y in sum_d) or (x - y) in diff_d:
                    continue
                #构建新的方案以及约束
                solute.append(y)
                diff_d.add(x - y)
                sum_d.add(x + y)
                count += dfs(solute, diff_d, sum_d, n)
                #回溯
                solute.pop()
                diff_d.remove(x - y)
                sum_d.remove(x + y)
            return count

        return dfs([], set(), set(), n)