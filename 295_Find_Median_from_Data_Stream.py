#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 295_Find_Median_from_Data_Stream.py
#time_complecity:  
#space_complecity: 
#beats: 

#数组
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.l = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        l, r = 0, self.l
        self.l += 1
        while l < r:
            m = l + (r - l)//2
            if self.nums[m] < num:
                l = m + 1
            else:
                r = m
        self.nums.insert(l, num)


    def findMedian(self):
        """
        :rtype: float
        """
        if self.l == 0: return None
        m = self.l//2
        if self.l & 1:
            return self.nums[m]
        return (self.nums[m] + self.nums[m - 1])/2.0


#堆
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []
        self.small = []
        self.len_large = 0
        self.len_small = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        #small中存的都是负值，这样保证small是一个最大堆
        if self.len_large == self.len_small:
            #将num加入small中，并从large中选择一个最小的，加入到small中
            heappush(self.small, -heappushpop(self.large, num))
            self.len_small += 1
        else:
            heappush(self.large, -heappushpop(self.small, -num))
            self.len_large += 1


    def findMedian(self):
        """
        :rtype: float
        """
        if self.len_small == 0: return None
        if self.len_large != self.len_small:
            return -self.small[0]
        return (self.large[0] - self.small[0])/2.0