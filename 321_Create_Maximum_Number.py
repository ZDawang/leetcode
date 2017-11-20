#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 321_Create_Maximum_Number.py
#time_complecity:  
#space_complecity: 
#beats: 
class Solution(object):
    #动态规划，可以使用三维数组dp[i][j][k]来表示nums1[:i],nums2[:j],表示的最大k位数，然后进行迭代。
    #dp[i][j][k] = max(dp(i-1,j,k), dp(i,j-1,k), dp(i-1,j,k-1) + [nums1[i]], dp(i,j-1,k-1) + [nums2[j]])

    #







nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
soltue = Solution()
res = soltue.maxNumber(nums1, nums2, 5)