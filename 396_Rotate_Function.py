#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 396_Rotate_Function
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def maxRotateFunction(self, A):
        l = len(A)
        temp = 0
        for i in range(l):
            temp += i*A[i]
        res = temp
        sumA = sum(A)
        for i in range(l):
            temp += sumA - l*A[l - i - 1]
            if temp > res:
                res = temp
        return res

A = [4, 3, 2, 6]
solute = Solution()
res = solute.maxRotateFunction(A)
print(res)