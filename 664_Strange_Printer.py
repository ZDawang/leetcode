#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 664_Strange_Printer.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP，使用dp[i][j]来表示i到j的最小次数
    #思路是如果有i到j的次数，那么i+1到j的次数，可以推导出来，
    #如果s[i+1] == s[j]或者s[i]，那么在之前扩展的时候就可以顺便扩展s[i+1]放在这里。
    #所以递归关系可以表示为
    #dp[i][j] = min(dp[i+1][j] + (s[i] != s[i+1]) and s[i] != s[j]), dp[i][j-1] + (s[j] != s[i] and s[j] != s[j-1])
    #可以看出，字符串长度是递增的，所以需要以长度作为遍历的对象。
    #空间复杂度可优化为O(n)，因为长度为n只用到了长度为n-1的dp
    
    #思路错误，没有考虑下面这种情况：
    #dcd abcbcddbccdcb
    #dcd需要2次，后面abcbcddbccdcb需要7次，总共需要9次，而cdabcbcddbccdcb需要9次，前面加一个d则按算法需要10次。
    #更新，再加一层迭代，dp[i][j] = min(dp[i][k-1] + dp[k+1][j]) if s[k] == s[i] or s[k] == s[j]
    #DFS+memo应该可以剪枝，懒的做了。。
    def strangePrinter(self, s):
        if not s: return 0
        ls = len(s)
        dp = [[0] * ls for _ in range(ls)]
        #初始化长度为0的时候
        for i in range(ls):
            dp[i][i] = 1
        #按子字符串长度遍历
        for l in range(1, ls):
            #i是子字符串开头的下标
            for i in range(ls - l):
                j = i + l
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
                #下面判断不到k==j的情况，所以在这里判断一下。
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                for k in range(i + 1, j):
                    if s[k] == s[i] or s[k] == s[i+l]:
                        dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k+1][j])
        return dp[0][-1]


s = "ccdcadbddbaddcbccdcdabcbcddbccdcbad"
solute = Solution()
res = solute.strangePrinter2(s)