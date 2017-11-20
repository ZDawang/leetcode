#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 207_Course_Schedule
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dfs(prec, c):
            if not c in d: return 1
            if c in prec: return 0
            prec.add(c)
            visit.add(c)
            for nextc in d[c]:
                if not dfs(prec, nextc):
                    return 0
            prec.remove(c)
            return 1
        #构建字典树
        d = {}
        for c1, c2 in prerequisites:
            if c1 in d:
                d[c1].append(c2)
            else:
                d[c1] = [c2]
        visit = set()
        for c in d:
            prec = set()
            if c in visit:
                continue
            if not dfs(prec, c):
                return False
        return True

solute = Solution()
numCourses = 2
prerequisites = [[1,0], [0,1]]
res = solute.canFinish(numCourses, prerequisites)