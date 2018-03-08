#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 788_Rotated_Digits.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP,二维dp[0][n]，记录开头为[0, 1, 8]，剩下长度为n的有效数字个数，
    #dp[1][n]，记录开头为[2,5,6,9]，剩下长度为n的有效数字个数。
    def rotatedDigits(self, N):
        #i表示遍历到了第几位，issame表示前缀是否有[2,5,6,9],isable表示前缀是否有[3, 4, 7]
        def dfs(i, issame):
            if i == n + 1 or isable:
                return
            #统计有多少个
            if issame:
                tmp = sum(dp[1][n - i] for j in range(int(N[i])) if j in set([0, 1, 2, 5, 6, 8, 9]))
                dfs.res += tmp
                dfs(i + 1, issame, int(N[i]) in [3, 4, 7])
            else:
                tmp = 0
                for j in range(int(N[i])):
                    if j in [0, 1, 8]:
                        tmp += dp[0][n - i]
                    elif j in [2, 5, 6, 9]:
                        tmp += dp[1][n - i]
                dfs.res += tmp
                dfs(i + 1, int(N[i]) in [2, 5, 6, 9], int(N[i]) in [3, 4, 7])
        if N < 10:
            return sum(1 for j in range(N + 1) if j in set([2, 5, 6, 9]))
        N = str(N)
        n = len(str(N)) - 1
        dp = [[0] * (n + 1) for _ in range(2)]
        dp[0][0], dp[1][0] = 1, 1
        dp[0][1], dp[1][1] = 4, 7
        for i in range(2, n + 1):
            dp[0][i] = 3 * dp[0][i - 1] + 4 * dp[1][i - 1]
            dp[1][i] = 7 * dp[1][i - 1]
        dfs.res = 0
        dfs(0, False)
        #最后一个数N
        dfs.res += (not any(s in {'3', '4', '7'} for s in N)) and any(s in {'2', '5', '6', '9'} for s in N)
        return dfs.res








