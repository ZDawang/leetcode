#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 738_Monotone_Increasing_Digits
#time_complecity:  
#space_complecity: 
#beats: 

from functools import reduce
class Solution(object):
    #第一思路：回溯
    #问题的思路在于找到需要减1的那一位。然后把这一位减1，后面的全变为9就可以了
    #因为会有重复的数，所以需要找重复的数的最前面一个。比如332，则需要找到第一个3.变为299
    def monotoneIncreasingDigits(self, N):
        numStr = list(map(int, str(N)))
        flag = 0
        #找到比前面数小的那一位,用flag来标识是否找到
        for i in range(1, len(numStr)):
            if numStr[i] < numStr[i - 1]:
                flag = 1
                break
        #因为它前面有可能是重复的数，所以向前遍历，直到找到不重复的数字
        if flag:
            i -= 1
            while i > 0 and numStr[i] == numStr[i - 1]:
                i -= 1
            numStr[i] -= 1
        return reduce(lambda x, y: x * 10 + y, numStr[:i+1] + [9] * (len(numStr) - i - 1), 0) if flag else N


N = 124345
solute = Solution()
res = solute.monotoneIncreasingDigits(N)