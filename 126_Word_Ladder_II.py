#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 126_Word_Ladder_II.py
#time_complecity:  
#space_complecity: 
#beats: 
from collections import deque
class Solution(object):
    #BFS, TLE
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if not endWord in wordSet: return []
        queue = deque([[beginWord]])
        res = []
        remove = set()
        while queue and not res:
            l = len(queue)
            remove = set()
            for j in range(l):
                words = queue.popleft()
                lastword = words[-1]
                for i in range(len(lastword)):
                    front, back = lastword[:i], lastword[i + 1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = front + c + back
                        if new_word in wordSet:
                            if new_word == endWord:
                                res.append(words + [new_word])
                            else:
                                queue.append(words + [new_word])
                                remove.add(new_word)
            for word in remove:
                wordSet.remove(word)
        return res




    def _add_path(self, tree, word, new_word, forward):
        if forward:
            tree[word].append(new_word)
        else:
            tree[new_word].append(word)

    def findLadders(self, beginWord, endWord, wordList):
        def construct_path(head, tail, tree):
            if head == tail:
                return [[head]]
            return [[head] + path for succ in tree[head] for path in construct_path(succ, tail, tree)]
        
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        begin = set([beginWord])
        end = set([endWord])
        
        tree = collections.defaultdict(list)
        path, pathes = [begin], []
        self.bfs(begin, end, tree, wordList, True)
        return construct_path(beginWord, endWord, tree)
    
    def bfs(self, begin, end, tree, wordList, forward):
        if not begin:
            return
        if len(begin) > len(end):
            return self.bfs(end, begin, tree, wordList, not forward)
        
        for word in (begin | end):
            wordList.discard(word)
        
        next_lv, finished = set(), False
        while begin:
            word = begin.pop()
            for i in xrange(len(word)):
                for x in string.ascii_lowercase:
                    new_word = word[:i] + x + word[i+1:]
                    if new_word in end:
                        self._add_path(tree, word, new_word, forward)
                        finished = True
                    if not finished and new_word in wordList:
                        next_lv.add(new_word)
                        self._add_path(tree, word, new_word, forward)
        
        if not finished:
            self.bfs(next_lv, end, tree, wordList, forward)








beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
solute = Solution()
res = solute.findLadders2(beginWord, endWord, wordList)