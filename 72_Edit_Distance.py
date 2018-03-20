#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 72_Edit_Distance
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DP, dp[i][j]代表word1的0-i 转为 word2的0-j所需要的最小步数
    #插入一个字母，删除一个字母，替代一个字母
    def minDistance(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        #dp存储 word1的0到i位 转为 word2的0到j位 所需要的最小步
        #因为有空字符这种情况，所以dp的大小为(l1+1)*(l2+1)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        #初始化word1长度为0与word2长度为0的情况
        for i in range(l1 + 1):
            dp[i][0] = i
        for j in range(l2 + 1):
            dp[0][j] = j
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                #当字母相等时，则不用操作，直接用前一个字符的结果
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j]
                #否则，分别使用替换，删除word1的元素，删除word2的元素来得到最小结果
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
        return dp[-1][-1]

word1 = "a"
word2 = "b"
solute = Solution()
res = solute.minDistance(word1, word2)

