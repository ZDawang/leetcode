#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 352_Data_Stream_as_Disjoint_Intervals.py
#time_complecity:  
#space_complecity: 
#beats: 


#思路，将结果用列表存起来，然后用二分搜索去确定所需要存放的位置。
#结果有插入，合并，归并，不做处理四种情况。
#时间复杂度，O(n2)

#寻找一种结构，插入，删除，寻找都为O(logn)的复杂度。
#二分查找树，时间复杂度O(nlogn)


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges:
    def __init__(self):
        self.intervals = []
    
    #寻找val在intervals中的位置
    def binSearch(self, val):
        if self.intervals and val < self.intervals[0].start:
            return -1
        l, r = 0, len(self.intervals) - 1
        while l < r:
            m = (l + r) >> 1
            if self.intervals[m + 1].start <= val:
                l = m + 1
            else:
                r = m
        return l

    def addNum(self, val):
        pos = self.binSearch(val)
        #插入
        if pos < 0:
            if self.intervals[0].start - 1 == val:
                self.intervals[0].start = val
            else:
                newInterval = Interval(val, val)
                self.intervals.insert(0, newInterval)
        elif (not self.intervals) or (val > self.intervals[pos].end + 1 and ((pos == len(self.intervals) - 1) or (val < self.intervals[pos + 1].start - 1))):
            newInterval = Interval(val, val)
            self.intervals.insert(pos + 1, newInterval)
        #不做处理
        elif self.intervals[pos].start <= val and self.intervals[pos].end >= val:
            return
        #合并或者归并
        elif self.intervals[pos].end + 1 == val:
            if pos != len(self.intervals) - 1 and self.intervals[pos + 1].start - 1 == val:
                self.intervals[pos].end = self.intervals[pos + 1].end
                self.intervals.pop(pos + 1)
            else:
                self.intervals[pos].end = val
        else:
            self.intervals[pos + 1].start = val
        return 

    def getIntervals(self):
        return self.intervals
        