#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 211_Add_and_Search_Word.py
#time_complecity:  
#space_complecity: 
#beats: 


class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        
    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    #DFS+剪枝
    def searchHelper(self, word, i, node):
        #若搜索完毕
        if i == len(word):
            return node.end
        #若不是正则
        if word[i] != ".":
            if not word[i] in node.children:
                return False
            return self.searchHelper(word, i + 1, node.children[word[i]])
        else:
            for c in node.children:
                if self.searchHelper(word, i + 1, node.children[c]):
                    return True
            return False

