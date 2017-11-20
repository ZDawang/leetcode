#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 127_Word_Ladder.py
#time_complecity:  
#space_complecity: 
#beats: 
from collections import deque
class Solution(object):
    #BFS
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        level = 1
        queue = deque([beginWord])
        while queue:
            lq = len(queue)
            level += 1
            for i in range(lq):
                qword = queue.popleft()
                for j in range(len(qword)):
                    front, back = qword[:j], qword[j + 1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = front + c + back
                        if new_word in wordSet:
                            if new_word == endWord: return level
                            queue.append(new_word)
                            wordSet.remove(new_word)
        return 0

    #双端BFS
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if not endWord in wordSet:
            return 0
        ladderLen = 1
        beginSet = set([beginWord])
        endSet = set([endWord])
        while beginSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            nextLevel = set()
            for word in beginSet:
                for i in range(len(word)):
                    firstHalf, secondHalf = word[:i], word[i + 1:]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = firstHalf + ch + secondHalf
                        if newWord in endSet:
                            return ladderLen + 1
                        if newWord in wordSet:
                            nextLevel.add(newWord)
                            wordSet.remove(newWord)
            beginSet = nextLevel
            ladderLen += 1
        return 0

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
solute = Solution()
res = solute.ladderLength(beginWord, endWord, wordList)