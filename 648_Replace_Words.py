#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 648_Replace_Words.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution1(object):
    #hash,对每个词进行扫描，看是否有词根在字典中。若有则加入词根，否则加入词
    def replaceWords2(self, dict, sentence):
        d = set(dict)
        sentence = sentence.split(" ")
        res = []
        for s in sentence:
            replace = False
            for i in range(1, len(s) + 1):
                if s[:i] in d:
                    res.append(s[:i])
                    replace = True
                    break
            if not replace:
                res.append(s)
        return " ".join(res)


#Trie 字典树
class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    #插入
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True if word else False
    #查找
    def search(self, word):
        cur = self.root
        res = ""
        for c in word:
            #若匹配不到字母，则停止
            if not c in cur.children:
                break
            res += c
            cur = cur.children[c]
            #如果是词根，则停止
            if cur.end:
                break
        #是否为词根
        return res if cur.end else word

class Solution(object):
    def replaceWords(self, dict, sentence):
        #创建字典树
        trie = Trie()
        for s in dict: 
            trie.insert(s)
        return " ".join([trie.search(s) for s in sentence.split(" ")])




dict = ["a", "aa", "aaa", "aaaa"]

sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
solute = Solution()
res = solute.replaceWords(dict, sentence)