#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 480_Sliding_Window_Median
#time_complecity:  
#space_complecity: 
#beats: 

import heapq
from collections import defaultdict
class Solution(object):
    #两个堆+一个哈希表
    #smallheap为大根堆，bigheap为小根堆。
    #思路为：当一个数字来到时，不把i-k处的数字从堆中取出。而是放在fallset中。
    #两个堆的长度不一定为k，但有效长度均为k//2,若k为奇数，则smallHeap的长度为k//2+1
    #若k为奇数，则中位数为小根堆的最大值。若k为偶数，则中位数为小根堆最大值与大根堆最小值的平均。
    #时间复杂度，最优O(nlogk),最差O(nlogn)
    def medianSlidingWindow(self, nums, k):
        fallSet = defaultdict(int)
        smallHeap, bigHeap = [-num for num in nums[:k]], []
        balance = 0
        res = []
        #初始化堆
        heapq.heapify(smallHeap)
        for i in range(k//2):
            heapq.heappush(bigHeap, -heapq.heappop(smallHeap))
        #对k以后进行遍历
        for i in range(k, len(nums) + 1):
            #中位数
            if k & 1:
                res.append(float(-smallHeap[0]))
            else:
                res.append((-smallHeap[0] + bigHeap[0])/2.0)
            if i == len(nums):
                break
            balance = 0
            #将i-k放入fallSet中。
            if nums[i-k] <= -smallHeap[0]:
                balance -= 1
                if nums[i-k] == -smallHeap[0]:
                    heapq.heappop(smallHeap)
                else:
                    fallSet[nums[i-k]] += 1
            else:
                balance += 1
                if nums[i-k] == bigHeap[0]:
                    heapq.heappop(bigHeap)
                else:
                    fallSet[nums[i-k]] += 1
            #将新数字放入堆中。
            if smallHeap and nums[i] <= -smallHeap[0]:
                balance += 1
                heapq.heappush(smallHeap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(bigHeap, nums[i])
            #rebalance
            if balance < 0:
                heapq.heappush(smallHeap, -heapq.heappop(bigHeap))
            elif balance > 0:
                heapq.heappush(bigHeap, -heapq.heappop(smallHeap))
            #去除fallSet中数字。
            while smallHeap and fallSet[-smallHeap[0]] > 0:
                fallSet[-smallHeap[0]] -= 1
                heapq.heappop(smallHeap)
            while bigHeap and fallSet[bigHeap[0]] > 0:
                fallSet[bigHeap[0]] -= 1
                heapq.heappop(bigHeap)
        return res


    #O(nk)方法，维护一个有序窗。
    #TLE
    def medianSlidingWindow2(self, nums, k):
        def search(nums, num):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) >> 1
                if nums[m] < num:
                    l = m + 1
                else:
                    r = m
            return l

        def insert(nums, num):
            if not nums or num >= nums[-1]:
                nums.append(num)
                return
            #寻找插入位置
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) >> 1
                if nums[m] < num:
                    l = m + 1
                else:
                    r = m
            #移位
            nums.append(0)
            for i in range(len(nums) - 1, l - 1, -1):
                nums[i] = nums[i - 1]
            nums[l] = num

        window = sorted(nums[:k])
        medians = []
        for i in range(k, len(nums) + 1):
            if k & 1:
                medians.append(float(window[k//2]))
            else:
                medians.append((window[(k-1)//2] + window[k//2])/2.0)
            if i == len(nums): break
            window.pop(search(nums[i-k]))
            #将此处用bisect的insort就不会TLE了
            #insert(window, nums[i])
            bisect.insort(window, nums[i])
        return medians






nums = [2147483647,1,2,3,4,5,6,7,2147483647]
k = 2
solute = Solution()
res = solute.medianSlidingWindow2(nums, k)




