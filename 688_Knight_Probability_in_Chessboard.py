#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 688_Knight_Probability_in_Chessboard
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP。dp[k][i][j]代表第k步到(i, j)的结果数。
    #使用out来代表出去的次数。
    #若在第i步出去了，则应该为 out* (8**(k-i))，因为它后面的也都是出去的。
    def knightProbability(self, N, K, r, c):
        dp = [[[0] * N for _ in range(N)] for _ in range(k)]
        