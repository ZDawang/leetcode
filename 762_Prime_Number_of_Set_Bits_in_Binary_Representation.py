#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 762_Prime_Number_of_Set_Bits_in_Binary_Representation
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #对每个数都统计一下1的个数，并判断是否为素数
    #每个数都统计1的这里，可以用动态规划。dp[num] = dp[num >> 1] + num & 1
    def countPrimeSetBits(self, L, R):
        #判断一个数是否为素数
        #因为最多有32位，所以只用列出32以内的素数即可。
        #一种特殊算法，因为大于等于5的素数都在6的倍数相邻，比如11与13,17与19等。
        def countBit(num):
            count = 0
            while num > 0:
                if num & 1: count += 1
                num = num >> 1
            return count

        count = 0
        primeSet = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        for num in range(L, R + 1):
            if countBit(num) in primeSet:
                count += 1
        return count

    def countPrimeSetBits2(self, L, R):
        count = 0
        primeSet = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        for num in range(L, R + 1):
            if bin(num)[2:].count('1') in primeSet:
                count += 1
        return count

L, R = 244,269
solute = Solution()
res = solute.countPrimeSetBits(L, R)
