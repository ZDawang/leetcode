#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-6-28
#difficulty degree：
#problem: 413_Arithmetic_Slices
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        l = len(A)
        if l < 3:
            return 0
        diff = A[1] - A[0]
        len_diff = []
        len_temp = 1
        for i in range(2, l):
            if A[i] - A[i - 1] == diff:
                len_temp += 1
            else:
                len_diff.append(len_temp)
                len_temp = 1
                diff = A[i] - A[i - 1]
        len_diff.append(len_temp)
        res = 0
        for d in len_diff:
            if d >= 2:
                res += d * (d - 1)//2
        return res

A = [1,2,3,8,9,10]
solute = Solution()
res = solute.numberOfArithmeticSlices(A)
print(res)
