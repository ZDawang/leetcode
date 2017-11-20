#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 56_merge_intervals
#time_complecity:  
#space_complecity: 
#beats: 


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda i:i.start)
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


intervals = [Interval(1,3),Interval(15,18),Interval(8,10),Interval(2,6)]
solute = Solution()
res = solute.merge(intervals)
for r in res:
    print(r.start, r.end)