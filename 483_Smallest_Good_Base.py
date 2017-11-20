#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-29
#difficulty degree：
#problem: 483_Smallest_Good_Base
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def smallestGoodBase(self, n):
        n = int(n)
        maxm = int(math.log(n, 2))
        for m in range(maxm, 1, -1):
            k = int(n**(m**-1))
            if (k**(m + 1) - 1)//(k - 1) == n:
                return str(k)
        return str(n - 1)
