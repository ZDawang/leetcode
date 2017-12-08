#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 668_Kth_Smallest_Number_in_Multiplication_Table.py
#time_complecity:  
#space_complecity: 
#beats: 

import heapq
class Solution(object):
    #第一思路，堆，时间复杂度，O(Klog(min(m, n)))
    #TLE
    def findKthNumber(self, m, n, k):
        if k >= m * n: return m * n
        m, n = min(m, n), max(m, n)
        heap = [(i, 1, i) for i in range(1, n + 1)]
        while k > 0:
            product, i, j = heapq.heappop(heap)
            if i < m:
                heapq.heappush(heap, (product + j, i + 1, j))
            k -= 1
        return product

    #第二思路，二分法，时间复杂度O(mlog(mn))
    def findKthNumber2(self, m, n, k):
        #统计m*n中小于等于mid的数量
        def count(m, n, mid):
            res = 0
            for i in range(1, m + 1):
                #第i行，小于等于mid的个数为mid//i，同时最多有n个，所以是min(mid // i, n)
                res += min(mid // i, n)
            return res
        #二分
        l, r = 0, m * n
        while l < r:
            mid = (l + r)//2
            if count(m, n, mid) < k:
                l = mid + 1
            else:
                r = mid
        return l

    #优化，时间复杂度O(min(m, n)log(m, n))
    #因为m*n与n*m是一样的。所以可以把m变为min(m,n)，优化时间复杂度
    #defeat：96.39%
    def findKthNumber3(self, m, n, k):
        #统计m*n中小于等于mid的数量
        def count(m, n, mid):
            res = 0
            for i in range(1, m + 1):
                #第i行，小于等于mid的个数为mid//i，同时最多有n个，所以是min(mid // i, n)
                res += min(mid // i, n)
                #要是这里换成下面，可以减少很多时间。。。
                #t = mid // i
                #if t > n: t = n
                #res += t
            return res

        #二分
        m, n = min(m, n), max(m, n)
        l, r = 0, m * n
        while l < r:
            mid = (l + r)//2
            if count(m, n, mid) < k:
                l = mid + 1
            else:
                r = mid
        return l

m, n, k = 45, 12, 471

solute = Solution()
res = solute.findKthNumber(m, n, k)
