#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 690_Employee_Importance.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS
    def getImportance(self, employees, id):
        def dfs(id):
            if id in visit: return 0
            visit.add(id)
            return sum([dfs(x) for x in subord[id]]) + value[id]
        
        visit = set()
        value, subord = {}, {}
        for employee in employees:
            value[employee.id] = employee.importance
            subord[employee.id] = employee.subordinates
        return dfs(id)
                

