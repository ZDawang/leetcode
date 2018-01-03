#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 472_Concatenated_Words.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS。对于一个词，若它的前缀在words中，则将剩下的继续DFS。
    #TLE, range的原因。
    def findAllConcatenatedWordsInADict(self, words):
        def dfs(word, start):
            #若word不是""，且遍历到最后。
            if word and start == len(word): return True
            canForm = False
            #此处换成xrange，就不会TLE。而且在百分之60处。。。。。
            for end in range(start + 1, len(word) + 1):
                if word[start: end] in wordSet:
                    canForm = dfs(word, end)
                if canForm:
                    break
            #若word可以由wordSet中的词构成，且不是由它本身。
            return canForm and not (start == 0 and end == len(word))

        wordSet = set(words)
        return [word for word in words if dfs(word, 0)]

    #DFS2，对于一个词，若它的后缀在words中，则剩下的继续。
    def findAllConcatenatedWordsInADict2(self, words):
        def dfs(word, end):
            if word and end == 0: return True
            canForm = False
            for start in range(end):
                #防止匹配它本身
                if start == 0 and end == len(word):
                    continue
                if word[start: end] in wordSet:
                    canForm = dfs(word, start)
                if canForm:
                    break
            return canForm

        wordSet = set(words)
        return [word for word in words if dfs(word, len(word))]

    #DP
    #对每一个单词，dp[i]表示它的前i位是否可以由wordSet中的词组成。
    def findAllConcatenatedWordsInADict3(self, words):
        def canForm(word):
            if not word: return False
            dp = [True] + [False] * len(word)
            for i in range(1, len(word) + 1):
                for j in range(i):
                    #去除匹配自身
                    if (j == 0 and i == len(word)):
                        continue
                    if dp[j] and word[j: i] in wordSet:
                        dp[i] = True
                        break
            return dp[-1]

        wordSet = set(words)
        return [word for word in words if canForm(word)]

    #字典树
    #DFS + Trie
    #只是在DFS的时候，把word[start: end] in wordSet换成检查当前node是否为叶node。
    #range改为xrange，才能不TLE。
    def findAllConcatenatedWordsInADict4(self, words):
        trie = Trie()
        words.sort(key = lambda x: len(x))
        res = []
        for word in words:
            if trie.canForm(word, 0):
                res.append(word)
            trie.insert(word)
        return res

class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True if word else False

    def canForm(self, word, start):
        if word and start == len(word): return True
        cur = self.root
        #这里改为xrange，不会TLE
        for end in range(start, len(word)):
            c = word[end]
            #若当前字符串不在字典树中，则返回False
            if not c in cur.children:
                return False
            if cur.children[c].end:
                if self.canForm(word, end + 1):
                    return True
            cur = cur.children[c]
        return False

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
solute = Solution()
res = solute.findAllConcatenatedWordsInADict4(words)
