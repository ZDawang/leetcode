#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #O(sqrt(n))
    def isPerfectSquare(self, num):
        i = 0
        while(i*i < num):
            i += 1
        return i*i == num
    #O(logn),二分法
    def isPerfectSquare2(self, num):
        l, r = 0, num
        while(l < r):
            m = l + (r - l)//2
            if m * m < num:
                l = m + 1
            else:
                r = m
        return l * l == num
    #牛顿法
    #x = xk - (xk*xk - num)/2xk = 0.5(xk + xk/num)
    def isPerfectSquare3(self, num):
        x = num
        while(x * x > num):
            x = (x + num//x)//2
            print(x)
        return x * x == num


solute = Solution()
res = solute.isPerfectSquare3(9)
print(res)