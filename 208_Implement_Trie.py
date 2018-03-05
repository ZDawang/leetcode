#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 
#time_complecity:  
#space_complecity: 
#beats: 

class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word):
        node = self.root
        for c in word:
            if not c in node.children:
                return False
            node = node.children[c]
        return node.end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if not c in node.children:
                return False
            node = node.children[c]
        return True
