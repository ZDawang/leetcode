#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 347_Top_K_Frequent_Elements.py
#time_complecity:  
#space_complecity: 
#beats: 
from collections import Counter
import heapq
from collections import defaultdict
class Solution(object):
    #第一思路，堆。
    #维护一个大小为k的最小堆。当新数字次数比堆中最小次数还小的话，则不加入堆
    #否则加入堆，且把堆中最小次数弹出。
    #最终剩下的就是次数最多的k个。
    #时间复杂度O(nlogk)
    def topKFrequent(self, nums, k):
        counts = Counter(nums).items()
        #初始化堆。
        heap = [(count, num) for num, count in counts[:k]]
        heapq.heapify(heap)
        for num, count in counts[k:]:
            if count <= heap[0][1]:
                continue
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        return [num for (count, num) in heap]

    #桶排序
    #以出现次数作为桶。数字作为桶中的元素。
    #时间复杂度O(n)
    def topKFrequent2(self, nums, k):
        counts = Counter(nums)
        #创建桶
        bucket = defaultdict(list)
        for num, count in counts.items():
            bucket[count].append(num)
        res = []
        #出现次数在1到len(nums)中
        for count in range(len(nums), 0, -1):
            #若没有当前次数，则continue
            if not count in bucket:
                continue
            if k <= 0:
                break
            res += bucket[count]
            k -= len(bucket[count])
        return res

    #快排思路
    #时间复杂度O(n)-O(n2),平均O(n)
    def topKFrequent3(self, nums, k):
        def partion(l, r, k):
            #分区
            pivot = counts[l]
            i, j = l, r
            while i < j:
                while i < j and counts[j][1] >= pivot[1]:
                    j -= 1
                counts[i] = counts[j]
                while i < j and counts[i][1] <= pivot[1]:
                    i += 1
                counts[j] = counts[i]
            counts[i] = pivot
            #对分区结果进行选择
            if i == len(counts) - k:
                return
            elif i < len(counts) - k:
                partion(i + 1, r, k)
            else:
                partion(l, i - 1, k)

        counts = Counter(nums).items()
        counts = [[num, count] for (num, count) in counts]
        partion(0, len(counts) - 1, k)
        return [num for (num, count) in counts[len(counts) - k:]]

nums = [1,1,1,2,2,3]
k = 2
solute = Solution()
res = solute.topKFrequent3(nums, k)