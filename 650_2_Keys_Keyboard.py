#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 650_2_Keys_Keyboard
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp存储的为获得数量为下标的字母，所需要的最小次数以及当前复制的个数(思路不可行，因为同样数量，复制个数也不相同，所以为2维dp)
    #dp[i][j] = k, 表示获得数量为i的字母，当前复制的字母个数为j，所需要的步数最小为k
    #TLE
    def minSteps(self, n):
        maxstep = float("inf")
        dp = [[maxstep] * (n + 1) for i in range(n + 1)]
        dp[1][0] = 0
        for i in range(1, n):
            #复制操作
            dp[i][i] = min(dp[i]) + 1
            #粘贴操作
            for j in range(1, i + 1):
                if i + j <= n:
                    dp[i + j][j] = min(dp[i + j][j], dp[i][j] + 1)
        return min(dp[n])

    #一维DP，当i%j==0时，这是i最小的次数为dp[j] + i//j,j为i的最大约数
    def minSteps2(self, n):
        dp = [0] * (n + 1)
        res = 0
        while(n > 1):
            for i in range(2, n + 1):
                if n % i == 0:
                    n = n // i
                    res += i
                    break
        return res



n = 11
solute = Solution()
res = solute.minSteps2(n)
