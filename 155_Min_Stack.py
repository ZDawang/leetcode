#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 155_Min_Stack.py
#time_complecity:  
#space_complecity: 
#beats: 

import heapq
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minnum = float("inf")
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.minnum:
            self.stack.append(self.minnum)
            self.minnum = x
        self.stack.append(x)
        
        

    def pop(self):
        """
        :rtype: void
        """
        if(self.stack.pop() == self.minnum):
            self.minnum = self.stack.pop();
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1];
        
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minnum

stack = MinStack()
stack.push(3)
stack.push(2)
stack.push(1)