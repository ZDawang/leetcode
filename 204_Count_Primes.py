#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-
#difficulty degree：
#problem: 204_Count_Primes
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE，扫描方式
    def countPrimes(self, n):
        res = 0
        for i in range(2, n):
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    flag = 1
                    break
            if not flag: res += 1
        return res

    #思考：质数与前面的数有什么关系吗？若一个数能除以前面的质数余数都不为0，那么就是质数,所以只用除前面的质数
    #仍然LTE。。。。
    def countPrimes2(self, n):
        res = []
        for i in range(2, n):
            flag = 0
            for r in res:
                if i % r == 0:
                    flag = 1
                    break
            if not flag: res.append(i)
        return len(res)

    #巧妙，不找质数，找非质数。。。
    def countPrimes3(self, n):
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)




n = 499979
solute = Solution()
res = solute.countPrimes2(n)
print(res)