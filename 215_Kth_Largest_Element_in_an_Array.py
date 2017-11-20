#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 215_Kth_Largest_Element_in_an_Array.py
#time_complecity:  
#space_complecity: 
#beats: 

import heapq

class Solution(object):
    #堆，复杂度为O(n) + O(k+(n-k)lgk)
    def findKthLargest2(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


    def findKthLargest(self, nums, k):
        #改动的分区函数，大的数放前面
        def partion(nums, l, r):
            i, j = l, r
            pivot = nums[i]
            while i < j:
                #右侧扫描
                while i < j and nums[j] <= pivot:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                #左侧扫描
                while i < j and nums[i] >= pivot:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            return i

        partloc = partion(nums, 0, len(nums) - 1)
        if partloc == k - 1: 
            return nums[partloc]
        #若左分区数量太多
        elif partloc > k - 1:
            return self.findKthLargest(nums[:partloc], k)
        else:
            return self.findKthLargest(nums[partloc + 1:], k - partloc - 1)



    

