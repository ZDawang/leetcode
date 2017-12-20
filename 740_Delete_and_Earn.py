#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 740_Delete_and_Earn
#time_complecity:  
#space_complecity: 
#beats: 

from collections import Counter
class Solution(object):
    #DP
    #使用dp[i]来存储到第i小个数，且删除第i小个数所获得的最大分数
    #所以如果第i小个数=第i-1小个数+1：dp[i] = max(dp[j] for j in range(i - 1)) + n * c
    #否则dp[i] = max(dp[j] for j in range(i)) + n * c
    #空间O(n)，时间最差O(nlogn)(排序)
    def deleteAndEarn(self, nums):
        if not nums: return 0
        #计数并从小到大排序
        count = sorted(Counter(nums).items(), key = lambda x: x[0])
        dp = [0] * len(count)
        #用来存放0到第i-2个数(包括第i-2)的最大点数。
        maxpoint = 0   
        for i, (n, c) in enumerate(count):
            if n - 1 == count[i - 1][0]:
                dp[i] = maxpoint + n * c
            else:
                dp[i] = max(maxpoint, dp[i - 1]) + n * c
            maxpoint = max(maxpoint, dp[i - 1])
        return max(dp[-1], maxpoint)

    #优化空间复杂度,O(1)，错了，还是O(n),count占的空间
    def deleteAndEarn2(self, nums):
        count = sorted(Counter(nums).items(), key = lambda x: x[0])
        cur, pre, mp = 0, 0, 0
        for i, (n, c) in enumerate(count):
            cur = (mp if n - 1 == count[i - 1][0] else max(mp, pre)) + n * c
            mp, pre = max(mp, pre), cur
        return max(cur, mp)


nums = [1,1,1,2,4,5,5,5,6]
solute = Solution()
res = solute.deleteAndEarn(nums)