#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-23
#difficulty degree：
#problem: 600_Non-negative_Integers_without_Consecutive_Ones
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #n最大为10e9，所以不能用dp数组存储每一个数
    #存储2,4,8,16。。。以下的结果 dp(k) = k // 4 + dp(k/2) + dp(k / 4)
    #对于一个数，比如110，大于96的部分全部包含连续1，小于96部分直接由dp算出
    #若对于90，则先计算64以下的，对于64到90的，等于0到26，重复跌打得出最终结果
    def findIntegers(self, num):
        #dp
        dp = [0, 0]
        power = 4
        while(power <= num):
            dp.append(power//4 + dp[-1] + dp[-2])
            power *= 2
        res = 0
        newnum = num
        while(num > 2):
            k = 1
            while(2 ** k <= num):
                k += 1
            k -= 1
            if num >= 2**(k - 1) * 3:
                res += num - (2**(k - 1) * 3) + 1 + dp[k] + dp[k - 1]
                return newnum - res + 1
            else:
                res += dp[k]
                num -= 2 ** k
        return newnum - res + 1


solute = Solution()
res = solute.findIntegers(13)
