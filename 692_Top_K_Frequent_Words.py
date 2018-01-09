#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 692_Top_K_Frequent_Words
#time_complecity:  
#space_complecity: 
#beats: 

from collections import Counter
import heapq
class Solution(object):
    #堆, 使用堆来寻找第k少的数量。
    #维护一个大小为k的堆,则最后剩下的则就是出现次数最多的。
    #
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap, res = [], [""]
        #维护大小为k的堆，对出现次数进行筛选
        for word in count:
            heapq.heappush(heap, (count[word], word))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]
        

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
solute = Solution()
res = solute.topKFrequent(words, k)
