#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 718_Maximum_Length_of_Repeated_Subarray.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #双指针。
    #将B进行移位。然后对比，找出最长的相同子串。
    #然后将A进行移位，进行对比，找出最长的相同子串。
    #O(n2)
    def findLength(self, A, B):
        def helper(A, B):
            la, lb = len(A), len(B)
            start, res = 0, 0
            while start < lb:
                #寻找最大匹配长度。
                tmp = 0
                for i in range(la):
                    if start + i >= lb:
                        break
                    if B[start + i] == A[i]:
                        tmp += 1
                    else:
                        tmp = 0
                    res = max(res, tmp)
                start += 1
            return res
        return max(helper(A, B), helper(B, A))

    #DP，使用dp[i][j]存储 A[:i]与B[:j]的最长的子串长度。
    #空间复杂度可优化。
    def findLength2(self, A, B):
        la, lb = len(A), len(B)
        dp = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]
        for i in range(la):
            for j in range(lb):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max(dp[i][j] for i in range(la + 1) for j in range(lb + 1))

    #二分，对子串长度进行二分查找
    #时间复杂度，O((la + lb)*log(min(la, lb)),空间复杂度O(min(la, lb) ** 2)
    def findLength3(self, A, B):
        #检查长度为m的相同子串是否存在。
        def isExist(A, B, m):
            setA = set([tuple(A[i: i+m]) for i in range(len(A) - m + 1)])
            return any(tuple(B[i: i+m]) in setA for i in range(len(B) - m + 1))

        l, r = 0, min(len(A), len(B))
        while l < r - 1:
            m = l + (r - l)//2
            if isExist(A, B, m):
                l = m
            else:
                r = m - 1
        return r if isExist(A, B, r) else l 




A = [0,0,0,0,0]
B = [0,0,0,0,0]
solute = Solution()
res = solute.findLength3(A, B)