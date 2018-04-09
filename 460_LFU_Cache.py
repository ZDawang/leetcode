#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 460_LFU_Cache.py
#time_complecity:  
#space_complecity: 
#beats: 

#不知道哪里出问题了。。。
class LinkList(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prior = None
        self.next = None

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = LinkList("start", "start")
        self.end = LinkList("end", "end")
        self.connect(self.start, self.end)
        self.pos = {} #记录key对应的node位置。
        self.freqpos = {0: self.start} #记录当前freq的最后一个位置
    
    def connect(self, node1, node2):
        node1.next = node2
        node2.prior = node1  
    
    #调整节点位置
    def adjust(self, node):
        node.freq += 1
        #找到要插入的位置，也就是当前频次的最后一个节点后面
        if not node.freq in self.freqpos:
            insert_node = self.end.prior
        else:
            insert_node = self.freqpos[node.freq]
        #更新freqpos
        if self.freqpos[node.freq - 1] == node:
            self.freqpos[node.freq - 1] = node.prior
        self.freqpos[node.freq] = node
        if insert_node == node:
            return
        #插入
        self.connect(node.prior, node.next)
        self.connect(node, insert_node.next)
        self.connect(insert_node, node)


    def get(self, key):
        if not key in self.pos:
            return -1
        node = self.pos[key]
        self.adjust(node)
        return node.val

    def put(self, key, value):
        if key in self.pos:
            self.adjust(self.pos[key])
            self.pos[key].val = value
        else:
            #若满，则先删除一个点
            if self.capacity == 0:
                deleteNode = self.start.next
                if deleteNode == self.end:
                    return
                #更新字典
                self.pos.pop(deleteNode.key)
                if self.freqpos[deleteNode.freq] == deleteNode:
                    self.freqpos[deleteNode.freq] = deleteNode.prior
                self.connect(self.start, self.start.next.next)
                self.capacity += 1
                del deleteNode
            #将新节点插入头节点下面，再调整
            node = LinkList(key, value)
            self.pos[key] = node
            self.connect(node, self.start.next)
            self.connect(self.start, node)
            node.freq -= 1
            self.adjust(node)
            self.capacity -= 1
    





class ListNode(object):
    def __init__(self, key, val):
        self.next = None
        self.prior = None
        self.key = key
        self.val = val

class HashLinkList(object):
    def __init__(self):
        self.pos = {}
        self.start = ListNode("start", "start")
        self.end = ListNode("end", "end")
        self.connect(self.start, self.end)
        self.length = 0

    def connect(self, node1, node2):
        node1.next = node2
        node2.prior = node1 

    def get(self, key):
        if not key in self.pos:
            return -1
        node = self.pos[key]
        return node.val

    def popleft(self):
        delk = self.start.next.key
        if delk == "end":
            return
        self.delkey(delk)
        return delk


    def insert(self, key, val):
        node = ListNode(key, val)
        self.connect(self.end.prior, node)
        self.connect(node, self.end)
        self.pos[key] = node
        self.length += 1

    def delkey(self, key):
        node = self.pos[key]
        self.connect(node.prior, node.next)
        del node
        self.length -= 1
        self.pos.pop(key)

    def setval(self, key, val):
        self.pos[key].val = val

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq = {}    #key:freq
        self.lists = {1: HashLinkList()}   #freq: HashLinkList
        self.minfreq = 1  #最小频次，删除节点时使用
        
    def get(self, key):
        if not key in self.freq:
            return -1
        f = self.freq[key]
        val = self.lists[f].get(key)
        self.freq[key] += 1
        #将key从f转移到f+1
        self.lists[f].delkey(key)
        if not (f+1) in self.lists:
            self.lists[f+1] = HashLinkList()
        self.lists[f+1].insert(key, val)
        #更新minfreq
        if self.minfreq == f and (self.lists[f].length == 0):
            self.minfreq += 1
        return val
        
    def put(self, key, value):
        if key in self.freq:
            self.lists[self.freq[key]].setval(key, value)
            self.get(key)
        else:
            #若满，则删除一个节点
            if self.capacity == 0:
                if self.lists[self.minfreq].length == 0:
                    return
                delkey = self.lists[self.minfreq].popleft()
                self.freq.pop(delkey)
                self.capacity += 1
            #加入新节点
            self.freq[key] = 1
            self.lists[1].insert(key, value)
            self.minfreq = 1
            self.capacity -= 1

