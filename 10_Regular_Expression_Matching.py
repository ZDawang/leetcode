#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-1
#difficulty degree：
#problem: 10_Regular_Expression_Matching
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp[i][j]来表示p的前i位是否能匹配j的前j位
    #主要是当p为"*"时，讨论不同情况
    #匹配0次：dp[i][j] = dp[i - 2][j]
    #匹配1次：dp[i][j] = dp[i - 1][j - 1] & (p[i - 2] == "." or p[i - 2] == s[j - 1])
    #匹配多次: dp[i][j] = dp[i][j - 1] & (p[i - 2] == "." or p[i - 2] == s[j - 1])

    #空间复杂度可优化为O(n)，不过懒的做了。。。

    def isMatch(self, s, p):
        if not p: return True if not s else False
        ls, lp = len(s), len(p)
        dp = [[False] * (ls + 1) for _ in range(lp + 1)]
        dp[0][0] = True
        if p[0] == "*":
            p = p[1:]
        for i in range(1, lp + 1):
            for j in range(ls + 1):
                #当p为字母时,当j为0时也就是匹配空字符串时，肯定为False
                if p[i - 1] != "." and p[i - 1] != "*":
                    dp[i][j] = dp[i - 1][j - 1] & (p[i - 1] == s[j - 1]) if j != 0 else False
                #当p为"."时
                elif p[i - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1] if j != 0 else False
                #当p为"*"时，讨论匹配0次的情况，匹配1次的情况以及匹配多次的情况
                else:
                    dp[i][j] = ((dp[i - 2][j]) or ((dp[i - 1][j - 1] or dp[i][j - 1]) & (p[i - 2] == "." or p[i - 2] == s[j - 1]))) if j != 0 else dp[i - 2][j]
        return dp[-1][-1]

s = ""
p = ".b*"

solute = Solution()
res = solute.isMatch(s, p)


        

