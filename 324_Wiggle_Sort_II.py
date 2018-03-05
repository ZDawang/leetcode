#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 324_Wiggle_Sort_II.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #先找到中位数，然后将小于中位数的放在偶数位，将大于中位数的放在奇数位。
    #使用快排寻找中位数
    def findMedian(self, nums):
        def findKthLargest(nums, k):
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
                return findKthLargest(nums[:partloc], k)
            else:
                return findKthLargest(nums[partloc + 1:], k - partloc - 1)

        n = len(nums)
        return findKthLargest(nums, n//2 + 1)


    #大于中位数的放在奇数位，且从前向后放。
    #小于中位数的放在偶数位。且从后向前方。
    #中位数填剩下的地方。
    #这样做的目的在于防止中位数放在一起，这样就不满足wiggle的定义了。

    #自己写的寻找第k大数会TLE。。。。
    def wiggleSort(self, nums):
        #median = self.findMedian(nums)
        median = heapq.nsmallest(len(nums) / 2 + 1, nums)[-1]
        n = len(nums)
        #将大于中位数的放在奇数位
        i, k = 1, 0
        j = n - 1 if (n & 1) else n - 2
        while k < n:
            #当前数小于等于中位数，或者当前位置已经做好处理后。
            if nums[k] == median or (k % 2 == 0 and k > j) or (k & 1 and k < i):
                k += 1
            elif nums[k] > median:
                nums[k], nums[i] = nums[i], nums[k]
                i += 2
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 2