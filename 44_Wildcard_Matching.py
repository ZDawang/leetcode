#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 44_Wildcard_Matching.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用dp，当p为"*"时，考虑以下情况
    #不匹配任何字符：dp[i][j] = dp[i - 1][j]
    #匹配一个字符：dp[i][j] = dp[i - 1][j - 1]
    #匹配多个字符：dp[i][j] = dp[i - 1][j - n]
    #所以，结果就是只要dp[i - 1][:j+1]中有True，就可以匹配成功
    #TLE
    #优化,将累加用state来计算。。仍然TLE
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        dp = [[False] * (ls + 1) for _ in range(lp + 1)]
        dp[0][0] = True
        #使用state来表示i-1层的状态
        for i in range(1, lp + 1):
            state = False
            for j in range(ls + 1):
                state = state or dp[i - 1][j]
                if p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1] if j != 0 else False
                elif p[i - 1] == "*":
                    dp[i][j] = state
                else:
                    dp[i][j] = dp[i - 1][j - 1] & (p[i - 1] == s[j - 1]) if j != 0 else False
        return dp[-1][-1]

    #dp改进空间复杂度，不知道哪里减少的时间。。。
    def isMatch2(self, s, p):
        ls, lp = len(s), len(p)
        dp = [True] + [False] * ls
        newdp = dp[:]
        for c in p:
            if c == "*":
                newdp[0] = dp[0]
                for i in range(1, ls + 1):
                    newdp[i] = newdp[i - 1] or dp[i]
            else:
                newdp[0] = False
                for i in range(1, ls + 1):
                    newdp[i] = dp[i - 1] and (c == s[i - 1] or c == "?")
            dp = newdp[:]
        return dp[-1]

    #更进一步，不用额外的空间
    def isMatch4(self, s, p):
        ls, lp = len(s), len(p)
        dp = [True] + [False] * ls
        for c in p:
            if c == "*":
                for i in range(1, ls + 1):
                    dp[i] = dp[i - 1] or dp[i]
            else:
                for i in range(ls, 0, -1):
                    dp[i] = dp[i - 1] and (c == s[i - 1] or c == "?")
                dp[0] = False
        return dp[-1]


    #贪心算法。
    #对于"*"，这样匹配：记录当前匹配的位置，若后面不成功，则回溯回来
    def isMatch3(self, s, p):
        ls, lp = len(s), len(p)
        si, pi, savesi, savepi = 0, 0, -1, -1
        while si < ls:
            #当匹配时，向后走
            if pi < lp and (p[pi] == s[si] or p[pi] == "?"):
                si, pi = si + 1, pi + 1
            #当为"*"时，记录此时pi的位置，将pi后的字符串与si后的字符串进行匹配。
            #这里si没有+1，是为了匹配空字符串。savesi = si+1，是下次匹配的起点。
            elif pi < lp and p[pi] == "*":
                savesi, savepi = si + 1, pi
                pi += 1
            #当匹配不成功时或者p已经匹配完时(说明*匹配的内容不对)，回溯
            elif savepi != -1:
                si, pi = savesi, savepi
            else:
                return False
        #正常情况下pi应该等于lp，若是不等于，看后面是否全是"*"来匹配空字符串
        return p[pi:].count("*") == lp - pi




s = "bbaaabbababbbbbabababaaabbabbaabbbbbaaabbbaaababbbbababbbbabbbababaabababbbbbbbababaaababababbbbaabbaaaabbbaaabbbaababbbbababbbbbabbabbaabaabbaabaabbbabaabbbbbabababbabaabbababbabbbbabbbbaaaaaaaabbaab"
p = "a**abaaa*b*aa*ba*****b*a*bb**bbab*a*aa**b***ba*a*aabb*bab**aa*ab*b**b*b*aabba******bbbb*aa*a****abb***b*"
solute = Solution()
res = solute.isMatch(s, p)
