#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 454_4Sum_II
#time_complecity:  
#space_complecity: 
#beats: 

import collections

class Solution(object):
    #TLE
    def fourSumCount2(self, A, B, C, D):
        d_A, d_B, d_C, d_D = {}, {}, {}, {}
        for num in A:
            d_A[num] = d_A.setdefault(num, 0) + 1
        for num in B:
            d_B[num] = d_B.setdefault(num, 0) + 1
        for num in C:
            d_C[num] = d_C.setdefault(num, 0) + 1
        for num in D:
            d_D[num] = d_D.setdefault(num, 0) + 1
        res = 0
        for num_a in d_A:
            for num_b in d_B:
                for num_c in d_C:
                    num_d = -num_a - num_b - num_c
                    if num_d in d_D:
                        print(num_a, num_b, num_c, num_d)
                        res += d_A[num_a] * d_B[num_b] * d_C[num_c] * d_D[num_d]
        return res

    #将4个数组分成两个数组
    def fourSumCount(self, A, B, C, D):
        d_AB = {}
        d_AB = collections.Counter(a + b for a in A for b in B)
        res = 0
        for c in C :
            for d in D :
                if -c - d in d_AB:
                    count += d_AB[-c-d]
        return res

    #果然什么都不用才是最快的。。。。。
    def fourSumCount(self, A, B, C, D):
        hashtable = {}
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count





solute = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
res = solute.fourSumCount(A, B, C, D)
print(res)