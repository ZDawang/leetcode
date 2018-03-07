#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 341_Flatten_Nested_List_Iterator.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import deque
class NestedIterator(object):
    #使用DFS来表里列表，使用队列存储数据
    def __init__(self, nestedList):
        def dfs(node):
            if node.isInteger():
                self.queue.append(node.getInteger())
            else:
                for n in node.getList():
                    dfs(n)

        self.queue = deque()
        for node in nestedList:
            dfs(node)
        print(self.queue)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return True if self.queue else False

