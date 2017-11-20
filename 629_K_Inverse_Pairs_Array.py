#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-
#difficulty degree：
#problem: 629_K_Inverse_Pairs_Array
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp[i][j]来记录长度为i时，有j对相反pair的所有可能结果数
    #dp[n+1][k] = sum_{x=0..n} dp[n][k-x]
    # dp[n][k] = dp[n-1][k]+dp[n-1][k-1]+dp[n-1][k-2]+...+dp[n-1][k+1-n+1]+dp[n-1][k-n+1]
    # dp[n][k+1] = dp[n-1][k+1]+dp[n-1][k]+dp[n-1][k-1]+dp[n-1][k-2]+...+dp[n-1][k+1-n+1]
    # ->
    # dp[n][k+1] = dp[n][k]+dp[n-1][k+1]-dp[n-1][k+1-n]
    def kInversePairs(self, n, k):
        if k > n*(n-1)/2 or k < 0:
            return 0
        dp = [1, 1] + [0]*(k - 1)
        for i in range(3, n + 1):
            newdp = [1] + [0] * k
            for j in range(1, k + 1):
                newdp[j] = newdp[j - 1] + dp[j]
                if (j >= i): newdp[j] -= dp[j - i]
            dp = newdp
        return (dp[-1]) % (10**9 + 7)

