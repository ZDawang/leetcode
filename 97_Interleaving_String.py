#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-26
#difficulty degree：
#problem: 97_Interleaving_String
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp[i][j][k]代表s3的k个字母对应s1的i个字母，s4的j个字母
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        dp[0][0] = 1
        for k in range(1, l3 + 1):
            newdp = [[0] * (l2 + 1) for i in range(l1 + 1)]
            for i in range(l1 + 1):
                for j in range(l2 + 1):
                    if dp[i][j] == 0:
                        continue
                    if j < l2 and s3[k - 1] == s2[j]:
                        newdp[i][j + 1] = 1
                    if i < l1 and s3[k - 1] == s1[i]:
                        newdp[i + 1][j] = 1
            dp = newdp
        return dp[-1][-1] == 1

    def isInterleave2(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2: return False
        dp = {(0, 0)}
        for k in range(1, l3 + 1):
            newdp = set()
            for (i, j) in dp:
                if i < l1 and s3[k - 1] == s1[i]:
                    newdp.add((i + 1, j))
                if j < l2 and s3[k - 1] == s2[j]:
                    newdp.add((i, j + 1))
            dp = newdp
        return True if dp else False






s1 = "a"
s2 = "b"
s3 = "a"
solute = Solution()
res = solute.isInterleave2(s1, s2, s3)
