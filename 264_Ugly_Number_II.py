#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-23
#difficulty degree：
#problem: 264_Ugly_Number_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用字典来存储已经确认为ugly number的数字 
    #TLE?
    def nthUglyNumber(self, n):
        d = {1: 1, 2: 1, 3: 1, 5: 1}
        res = 1
        l_res = 1
        i = 2
        while l_res < n:
            if i % 2 == 0:
                if i // 2 in d:
                    d[i] = 1
                    l_res += 1
                    res = i
            elif i % 3 == 0:
                if i // 3 in d:
                    d[i] = 1
                    l_res += 1
                    res = i
            elif i % 5 == 0:
                if i // 5 in d:
                    d[i] = 1
                    l_res += 1
                    res = i
            i += 1
        return res

solute = Solution()
res = solute.nthUglyNumber(20)
print(res)