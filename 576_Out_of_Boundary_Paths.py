#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-23
#difficulty degree：
#problem: 576_Out_of_Boundary_Paths
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp存储每一步以后的可能结果
    def findPaths(self, m, n, N, i, j):
        #构建字典，存储每个位置一步出界的操作数
        d = {}
        for k in range(m):
            for l in range(n):
                tmp = (k == 0) + (k == m - 1) + (l == 0) + (l == n - 1)
                if tmp != 0:
                    d[(k + 1, l + 1)] = tmp
        #计算每一步的位置可能数
        dp = [[0]*(n + 2) for k in range(m + 2)]
        dp[i + 1][j + 1] = 1
        res = 0
        for k in range(N):
            for key in d:
                res += dp[key[0]][key[1]] * d[key]
            newdp = [[0]*(n + 2) for i in range(m + 2)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    newdp[i][j] = dp[i - 1][j] + dp[i + 1][j] + dp[i][j + 1] + dp[i][j - 1]
            dp = newdp
        return res % (1000000007)

solute = Solution()
res = solute.findPaths(3,2,5,1,1)




