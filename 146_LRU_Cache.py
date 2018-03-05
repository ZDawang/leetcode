#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 146_LRU_Cache.py
#time_complecity:  
#space_complecity: 
#beats: 

class LinkList(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prior = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = LinkList("start", "start")
        self.end = LinkList("end", "end")
        self.start.next, self.end.prior = self.end, self.start
        self.pos = {} #记录key对应的node位置。

    #直接读值，若在d中，则更新node位置
    def get(self, key):
        if not key in self.pos:
            return -1
        node = self.pos[key]
        node.prior.next = node.next
        node.next.prior = node.prior
        node.prior, node.next = self.end.prior, self.end
        self.end.prior.next, self.end.prior = node, node
        return node.val

    def put(self, key, value):
        #当key在链表中，则直接更新，且把node拿到最后。
        if key in self.pos:
            node = self.pos[key]
            node.val = value
            node.prior.next = node.next
            node.next.prior = node.prior
            node.prior, node.next = self.end.prior, self.end
            self.end.prior.next, self.end.prior = node, node
        #插入新节点
        else:
            #没有容量时，先删除第一个节点。
            if self.capacity == 0:
                deleteKey = self.start.next.key
                self.start.next.next.prior = self.start
                self.start.next = self.start.next.next
                self.pos.pop(deleteKey)
                self.capacity += 1
            #将新节点插入尾部
            newNode = LinkList(key, value)
            newNode.prior, newNode.next = self.end.prior, self.end
            self.end.prior.next, self.end.prior = newNode, newNode
            self.pos[key] = newNode
            self.capacity -= 1
