#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS+剪枝
    #记录每个皇后所在的列，并按行加入皇后
    #新加入的行需要满足以下条件，1.不在同一列。2.不在斜线上。
    def solveNQueens(self, n):
        def dfs(res, solute, diff_d, sum_d, n):
            x = len(solute)
            if x == n:
                res.append(solute)
                return
            #对于每一列
            for y in range(n):
                if (y in solute) or (y - x in diff_d) or (y + x in sum_d):
                    continue
                newdiff_d, newsum_d = diff_d.copy(), sum_d.copy()
                newdiff_d.add(y - x)
                newsum_d.add(y + x)
                dfs(res, solute + [y], newdiff_d, newsum_d, n)

        res = []
        dfs(res, [], set(), set(), n)
        return [["."*i + "Q" + "."*(n-i-1) for i in solute] for solute in res]

solute = Solution()
res = solute.solveNQueens(8)
