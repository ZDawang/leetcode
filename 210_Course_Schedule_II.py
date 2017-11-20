#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 210_Course_Schedule_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #BFS
    def findOrder(self, numCourses, prerequisites):
        backward = [[] for i in range(numCourses)]
        forward = [[] for i in range(numCourses)]
        for p in prerequisites:
            backward[p[0]].append(p[1])
            forward[p[1]].append(p[0])
        #队列里面存放不需要前序课程的课，当遍历完以后，若不需要前序课程的课的数量不等于总课程数，则失败
        queue = [i for i in range(numCourses) if not backward[i]]
        curcourse = 0
        count = 0
        res = []
        while queue:
            curcourse = queue.pop(0)
            count += 1
            res.append(curcourse)
            for i in forward[curcourse]:
                backward[i].remove(curcourse)
                if not backward[i]:
                    queue.append(i)
        return res if count == numCourses else []




        