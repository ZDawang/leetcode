#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp存储石头数为n时，先拿石头的是否赢。
    #dp, dp[1] = True, dp[2] = True, dp[3] = True, dp[4] = False
    #dp[5]，可以看做先拿1个石头，让对方输，dp[6]可以看做拿两个石头，让对方输....
    #所以，4的倍数都会输，其它都会赢。
    def canWinNim(self, n):
        return n % 4 != 0
