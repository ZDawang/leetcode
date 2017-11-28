#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3- 8
#difficulty degree：medium
#problem: 5_longest_palindromic_substring
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):

    def longestPalindrome(self, s):
        res_len = 0
        res = ""
        l1 = len(s)
        if l1 == 1: return s
        for i in range(1, l1):
            #寻找奇数长度的回文子串
            for k_odd in range(1, min(i + 1, l1 - i)):
                #若找到长度大于最大长度的回文子串，更新，同时，若仍可以继续下去，则继续循环
                if (s[i - k_odd] == s[i + k_odd]):
                    if k_odd + k_odd + 1 > res_len:
                        res_len = k_odd + k_odd + 1
                        res = s[i-k_odd : i+k_odd+1]
                    continue
                else:
                #若找到长度大于最大长度的回文子串，更新，若已到当前子串的最大长度，跳出循环
                    if k_odd+k_odd-1 > res_len:
                        res_len = k_odd + k_odd - 1
                        res = s[i-k_odd+1 : i+k_odd]
                    break
            #寻找偶数长度的回文子串，思路同奇数
            for k_even in range(1, min(i, l1 - i) + 1):
                if (s[i-k_even] == s[i+k_even-1]):
                    if k_even + k_even > res_len:
                        res_len = k_even + k_even
                        res = s[i-k_even : i+k_even]
                    continue
                else:
                    if k_even + k_even -2 > res_len:
                        res_len = k_even + k_even -2
                        res = s[i-k_even+1: i+k_even-1]
                    break
            if i >= l1 - (res_len+1)//2:
                return res


    #第一思路，DP,O(n2)
    def longestPalindrome2(self, s):
        if not s: return ""
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        res, lres = s[0], 0
        for j in range(l):
            dp[j][j] = True
            for i in range(j):
                if s[i] == s[j] and (i == j - 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i > lres:
                        lres = j - i
                        res = s[i: j + 1]
        return res

    #第二思路，以每个字符为中心，查找当前字符的最长子串。
    #因为有奇偶长度。所以中心有2n-1个。
    #时间复杂度O(n)-O(n2)
    def longestPalindrome3(self, s):
        l = len(s)
        lres, res = -1, ""
        for m in range(2 * len(s) - 1):
            i, j = m//2, (m + 1)//2
            #寻找中心为m的最长回文子串
            while i >= 0 and j < l and s[i] == s[j]:
                i -= 1
                j += 1
            #从i+1到j-1为回文子串
            if lres <= (j - 1) - (i + 1) - 1:
                lres = j - i - 1
                res = s[i + 1: j]
        return res


    #最优解：Manacher’s Algorithm
    #马车夫算法，本质思想是，利用前面已经匹配过的信息，减少后面匹配的次数。
    #O(n)
    def longestPalindrome4(self, s):
        #首尾的@与%是为了防止匹配溢出。
        s = "@#" + "#".join(list(s)) + "#%"
        maxM, maxR = 1, 1
        P = [1] * len(s)
        for i in range(1, len(s) - 1):
            #当i小于R时，可以利用maxM匹配的信息以及前面对称的j(2*maxM-i)匹配的信息
            P[i] = min(P[2 * maxM - i], maxR - i) if i < maxR else 1
            #前面j的信息可能不够，继续计算i的半径
            while s[i + P[i]] == s[i - P[i]]:
                P[i] += 1
            #更新maxM与maxR
            if i + P[i] > maxR:
                maxR, maxM = i + P[i], i
        i = P.index(max(P))
        return "".join(s[i - P[i] + 1: i + P[i]].split("#"))



s = "abcdefgfedcbab"
solute = Solution()
res = solute.longestPalindrome5(s)
print(res)