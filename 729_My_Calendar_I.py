#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 729_My_Calendar_I.py
#time_complecity:  
#space_complecity: 
#beats: 

#分别用start以及end来代表开始日期与截止日期。
#若一个新的日历插入的位置不同，则说明有重复。
class MyCalendar(object):
    def __init__(self):
        self.startC = []
        self.endC = []

    def book(self, start, end):
        if start >= end:
            return False
        #因为end可以等于start，所以是插入左边
        l = bisect.bisect_left(self.startC, end)
        r = bisect.bisect_right(self.endC, start)
        if l != r:
            return False
        self.startC.insert(l, start)
        self.endC.insert(l, end)
        return True
