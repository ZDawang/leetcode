#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 502_IPO
#time_complecity:  
#space_complecity: 
#beats: 

from queue import PriorityQueue

class Solution(object):
    #贪心算法
    #对capital进行排序。使用堆，将本金足够的project加入到堆中。
    #每次交易选利润最大的。直到k次
    def findMaximizedCapital(self, k, W, Profits, Capital):
        heap = PriorityQueue()
        #按Captital排序
        project = sorted(zip(Capital, Profits))
        i = 0
        while k > 0:
            #把project本金小于W的加入堆
            while i < len(project) and project[i][0] <= W:
                heap.put(-project[i][1])
                i += 1
            if heap.empty():
                break
            #获取当前一轮能获取的最大利润
            W -= heap.get()
            k -= 1
        return W


k = 2
W = 0
Profits = [1,2,3]
Capital = [0,1,1]
solute = Solution()
res = solute.findMaximizedCapital(k, W, Profits, Capital)