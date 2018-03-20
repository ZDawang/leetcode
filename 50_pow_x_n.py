#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-1
#difficulty degree：
#problem: 50_pow_x_n
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #递归
    def myPow(self, x, n):
        def pow_2(x, n, res):
            if n <= 0:
                return res
            i, j = 2, 0
            temp = x
            while(i <= n):
                temp *= temp
                i *= 2
            i = i // 2
            n -= i
            res.append(temp)
            pow_2(x, n, res)
        if n == 0:
            return 1
        res = []
        if n >0:
            pow_2(x, abs(n), res)
        else:
            pow_2(1/x, abs(n), res)
        res_multi = 1
        for r in res:
            res_multi *= r
        return res_multi



    #迭代
    def myPow2(self, x, n):
        x_temp = x if n >= 0 else 1.0 / x
        n_abs, res = abs(n), 1
        while(n_abs > 0):
            i, j, temp = 2, 0, x_temp
            while(i <= n_abs):
                temp *= temp
                i *= 2
            i = i // 2
            n_abs -= i
            res *= temp
        return res

    #DFS+memo
    def myPow3(self, x, n):
        def dfs(x, k):
            if k == 1: return x
            if k in memo:
                return memo[k]
            tmp = dfs(x, k//2) * dfs(x, k//2 + (k & 1))
            memo[k] = tmp
            return tmp
        if n == 0:
            return 1
        memo = {}
        if n < 0:
            return dfs(1/x, abs(n))
        else:
            return dfs(x, n)

x = 3
n = -1
solute = Solution()
res = solute.myPow2(x, n)
print(res)