#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-21
#difficulty degree：
#problem: 646_Maximum_Length_of_Pair_Chain
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(n2), dp存储到当前pair的最大结果, TLE
    def findLongestChain(self, pairs):
        pairs = sorted(pairs, key = lambda x: x[0])
        l = len(pairs)
        dp = [1] * l
        for i in range(l):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    #O(nlogn)
    def findLongestChain2(self, pairs):
        pairs.sort(key = lambda x: x[1])
        cur, res = float("-inf"), 0
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                res += 1
        return res



pairs = [[3,4],[2,3],[1,2]]
solute = Solution()
res = solute.findLongestChain2(pairs)
