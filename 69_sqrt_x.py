#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 69_sqrt_x
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #二分法
    def mySqrt(self, x):
        l, r = 0, x
        mid = (l + r) // 2
        while(l <= r):
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1)*(mid + 1):
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return mid

    def mySqrt2(self, x):
        l, r = 0, x
        while(l < r):
            mid = (l + r) // 2
            if (mid + 1) * (mid + 1) <= x:
                l = mid + 1
            else:
                r = mid
        return l


solute = Solution()
#for i in range(50):
#    res = solute.mySqrt(i)
#    print(res)

res = solute.mySqrt2(1)
print(res)