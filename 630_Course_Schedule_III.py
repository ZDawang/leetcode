#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 630_Course_Schedule_III.py
#time_complecity:  
#space_complecity: 
#beats: 

import heapq
class Solution(object):
    #贪心法，到当前日期时，尽量学最多的课。
    #使用大根堆来存储已经学过的课的长度，当新课来的时候，如果新课无法加入，则将
    #堆顶拿出，这样来使得能够继续学习。
    def scheduleCourse(self, courses):
        if not courses:
            return 0
        heap = []
        courses.sort(key = lambda x: (x[1], x[0]))
        #已经用了多少天
        use_day = 0
        for (couse_len, stop_day) in courses:
            #若仍可以继续学习
            if use_day + couse_len <= stop_day:
                heapq.heappush(heap, -couse_len)
                use_day += couse_len
            #若不能学习,则把最长的那个课程拿出来，再学习。
            else:
                if heap and couse_len < -heap[0]:
                    use_day -= -heapq.heappop(heap)
                    heapq.heappush(heap, -couse_len)
                    use_day += couse_len
        return len(heap)
