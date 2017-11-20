#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 386_Lexicographical_Numbers.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #直接排序。。O(logn)
    def lexicalOrder(self, n):
        return sorted([i for i in range(1, n + 1)], key = lambda x: str(x))

    #DFS
    #O(n), TLE....,不知道哪里出的问题,应该是最后一层的剪枝吧
    def lexicalOrder2(self, n):
        def dfs(num, n):
            if num > n: return
            res.append(num)
            for i in range(10):
                dfs(num * 10 + i, n)
        res = []
        for i in range(1, 10):
            dfs(i, n)
        return res

    #DFS, O(n)
    def lexicalOrder3(self, n):
        def dfs(start, result, n):
            if start > n: return
            for i in range(start, min(n + 1, (start//10)*10+10)):
                result.append(i)
                dfs(i*10, result, n)

        result = []
        dfs(1, result, n)
        return result
        

        








solute = Solution()
res = solute.lexicalOrder2(13)