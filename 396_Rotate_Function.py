#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 396_Rotate_Function
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def maxRotateFunction(self, A):
        l = len(A)
        temp = 0
        for i in range(l):
            temp += i*A[i]
        res = temp
        sumA = sum(A)
        for i in range(l):
            temp += sumA - l*A[l - i - 1]
            if temp > res:
                res = temp
        return res

    #暴力解法就是把所有结果都算一遍，然后找出最大值。
    #但是其实分析一下就可以知道，有些运算时重复的。所以可以利用DP的思想，
    #利用上一次计算的结果，更快速的获得当前运算的结果。
    #使用dp[i]来存储旋转i-1的F(i)值。所以转移方程为：
    #dp[i] = dp[i - 1] + sum(A) - l * A[-i]
    def maxRotateFunction2(self, A):
        if not A: return 0
        l, sums = len(A), sum(A)
        dp = [0] * l
        #初始值
        dp[0] = sum(i * A[i] for i in range(l))
        for i in range(1, l):
            dp[i] = dp[i - 1] + sums - l * A[-i]
        return max(dp)

    #优化空间复杂度, O(1)
    def maxRotateFunction3(self, A):
        if not A: return 0
        l, sums = len(A), sum(A)
        dp = sum(i * A[i] for i in range(l))
        res = dp
        for i in range(1, l):
            dp += sums - l * A[-i]
            res = max(res, dp)
        return res


A = [4, 3, 2, 6]
solute = Solution()
res = solute.maxRotateFunction(A)
print(res)