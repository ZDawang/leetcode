#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-26
#difficulty degree：
#problem: 279_Perfect_Squares
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):

    l = 0
    dp = [0]

    #BFS, 看哪一步先走到
    def numSquares2(self, n):
        res = 0
        i = 1
        p = []
        while(i * i <= n):
            p.append(i * i)
            i += 1
        check = {n}
        res = 0
        while check:
            temp = {}
            res += 1
            for c in check:
                for pnum in p:
                    if c == pnum:
                        return res
                    if c < pnum:
                        break
                    temp.append(c - pnum)
            check = temp
        return res


    #DP
    def numSquares(self, n):
        print(self.l, self.dp)
        if n <= self.l:
            return self.dp[n]
        for i in range(self.l + 1, n + 1):
            mindp = n
            j = 1
            while i - j*j >= 0:
                mindp = min(mindp, self.dp[i - j*j] + 1)
                j += 1
            self.dp.append(mindp)
        self.l = n
        return self.dp[-1]


solute = Solution()
res = solute.numSquares(1)
res = solute.numSquares(2)
res = solute.numSquares(2)
res = solute.numSquares(2)
print(res)