#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 373_Find_K_Pairs_with_Smallest_Sums.py
#time_complecity:  
#space_complecity: 
#beats: 
from heapq import *
class Solution(object):
    #使用堆，O(klogk)
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        heap = []
        l1, l2 = len(nums1), len(nums2)
        #将nums1的元素与nums2的最小元素组合放进堆中,防止后面出现重复情况。
        for i in range(min(k, l1)):
            heap.append([nums1[i] + nums2[0], i, 0])
        i = 0
        res = []
        while i < k:
            if not heap: return res
            sumnum, i1, i2 = heapq.heappop(heap)
            #对于当前最小值的坐标组合，将nums2的坐标+1作为新的组合放入堆中。
            if i2 < l2 - 1:
                heapq.heappush(heap, [nums1[i1] + nums2[i2 + 1], i1, i2 + 1])
            res.append([nums1[i1], nums2[i2]])
            i += 1
        return res


