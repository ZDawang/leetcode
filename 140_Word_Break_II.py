#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 140_Word_Break_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #回溯，TLE
    def wordBreak(self, s, wordDict):
        def dfs(maxlenOfd, s, d, tmp, res):
            if not s:
                res.append(" ".join(tmp))
                return
            for i in range(1, min(maxlenOfd + 1, len(s) + 1)):
                if s[:i] in d:
                    dfs(maxlenOfd, s[i:], d, tmp + [s[:i]], res)
            return

        if not wordDict: return []
        d = set(wordDict)
        maxlenOfd = max([len(word) for word in wordDict])
        res = []
        dfs(maxlenOfd, s, d, [], res)
        return res

    #优化，因为DFS会重复计算i位的情况。所以如果计算过i位的情况，把它保存下来。
    def wordBreak2(self, s, wordDict):
        def dfs(memo, s, d, start):
            if start in memo: return memo[start]
            if start == len(s): return [[]]
            tmp = []
            for j in range(start + 1, len(s) + 1):
                if s[start: j] in d:
                    for solute in dfs(memo, s, d, j):
                        tmp.append([s[start: j]] + solute)
            memo[start] = tmp
            return tmp

        if not wordDict: return []
        memo = {}
        wordD = set(wordDict)
        res = dfs(memo, s, wordD, 0)
        return [" ".join(x) for x in res]

    #DP + DFS,TLE
    def wordBreak3(self, s, wordDict):
        def dfs(s, dp, res, start, tmp):
            if start == len(s):
                res.append(" ".join(tmp))
                return
            for end in dp[start]:
                dfs(s, dp, res, end, tmp + [s[start: end]])


        if not wordDict: return []
        d = set(wordDict)
        maxlenOfd = max([len(word) for word in wordDict])
        dp = [[] for _ in range(len(s))]
        l = len(s)
        #构建dp数组
        for i in range(l):
            for j in range(i + 1, min(i + maxlenOfd + 1, l + 1)):
                if s[i: j] in d:
                    dp[i].append(j)
        #DFS
        res = []
        dfs(s, dp, res, 0, [])
        return resssssssss




s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
solute = Solution()
res = solute.wordBreak3(s, wordDict)