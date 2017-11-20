#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 87_Scramble_String.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def isScramble(self, s1, s2):
        l, l2 = len(s1), len(s2)
        if l != l2: return False
        dp = [[[False] * (l + 1) for i in range(l)] for j in range(l)]
        for k in range(1, l + 1):
            for i in range(l - k + 1):
                for j in range(l - k + 1):
                    if k == 1:
                        dp[i][j][k] = True if s1[i] == s2[j] else False
                    else:
                        for q in range(1, k):
                            if dp[i][j][k]: break
                            dp[i][j][k] = (dp[i][j][q] and dp[i + q][j + q][k - q]) or (dp[i][j + k - q][q] and dp[i + q][j][k - q])
        return dp[0][0][-1]
    


    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False;
        s3 = s2[::-1]
        if s1 == s2 or s1 == s3:
            return True;
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        count3 = collections.defaultdict(int)
        for idx in xrange(1, len(s1)):
            count1[s1[idx-1]] += 1
            count2[s2[idx-1]] += 1
            count3[s3[idx-1]] += 1
            if (count1 == count2 and 
                self.isScramble(s1[:idx], s2[:idx]) and
                self.isScramble(s1[idx:], s2[idx:])):
                return True
            if (count1 == count3 and 
                self.isScramble(s1[:idx], s3[:idx]) and
                self.isScramble(s1[idx:], s3[idx:])):
                return True
        return False

