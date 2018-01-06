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
    #最后的dp[k]则为第k步以后仍然在棋盘中的所有可能结果及次数。
    #所以概率就等于sum(dp)/8**k
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        direction = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        for k in range(K):
            newdp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if dp[i][j] == 0:
                        continue
                    for dx, dy in direction:
                        #若向一个方向走后，仍然在棋盘内
                        if 0 <= i + dx < N and 0 <= j + dy < N:
                            newdp[i + dx][j + dy] += dp[i][j]
            dp = newdp
        return float(sum(dp[i][j] for i in range(N) for j in range(N))) / 8 ** K
        