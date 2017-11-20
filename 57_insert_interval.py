#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 57_insert_interval
#time_complecity:  
#space_complecity: 
#beats: 


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        i = 0
        if not intervals:
            return []
        temp = intervals[0]
        for interval in intervals:
            if interval.start <= temp.end:
                temp.end = max(interval.end,temp.end)
            else:
                intervals[i], temp, i = temp, interval, i + 1
        return intervals[:i] +[temp]
    def insert(self, intervals, newInterval):
        #插入
        if not intervals:
            return [newInterval]
        len_intervals = len(intervals)
        l, r = 0, len_intervals - 1
        mid = 0
        if newInterval.start > intervals[-1].start:
            mid = len_intervals
            intervals = intervals + [newInterval]
        else:
            while(l <= r):
                mid = (l + r) // 2
                if intervals[mid].start < newInterval.start <= intervals[mid + 1].start:
                    mid += 1
                    break
                if newInterval.start <= intervals[mid].start:
                    r = mid - 1
                else:
                    l = mid + 1
            intervals.insert(mid, newInterval)

        #merge
        mid_temp = mid - 1 if mid >= 1 else 0
        res = self.merge(intervals[mid_temp:])
        return intervals[:mid_temp] + res

            

intervals = [Interval(1,5)]
solute = Solution()
res = solute.insert(intervals, Interval(2,3))
for r in res:
    print(r.start, r.end)
