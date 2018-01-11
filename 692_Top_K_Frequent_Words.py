#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 692_Top_K_Frequent_Words
#time_complecity:  
#space_complecity: 
#beats: 

from collections import Counter
from collections import defaultdict
import heapq
class Solution(object):
    #堆, 使用堆来寻找第k少的数量。
    #维护一个大小为k的堆,则最后剩下的则就是出现次数最多的。
    #因为python堆没法设置lambda函数，所以自定义一种对象。。
    #时间复杂度O(nlogk)
    def topKFrequent(self, words, k):
        class Element(object):
            def __init__(self, word, count):
                self.word = word
                self.count = count

            def __lt__(self, other):
                if self.count == other.count:
                    return self.word > other.word
                return self.count < other.count

            def __eq__(self, other):
                return self.count == other.count and self.word == other.word


        counts = Counter(words)
        heap, res = [], []
        #维护大小为k的堆，对出现次数进行筛选
        for word, count in counts.items():
            heapq.heappush(heap, (Element(word, count), word))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]
        
    #桶 + 字典树
    #使用桶来记录出现次数为i的单词，使用字典树来对桶中的单词进行排序。
    #时间复杂度O(n)
    def topKFrequent2(self, words, k):
        class TrieNode(object):
            def __init__(self):
                self.word = False
                self.children = {}

        class Trie(object):
            def __init__(self):
                self.root = TrieNode()

            def build(self, words):
                for word in words:
                    self.insert(word)

            def insert(self, word):
                if not word: return
                root = self.root
                for c in word:
                    if not c in root.children:
                        root.children[c] = TrieNode()
                    root = root.children[c]
                root.word = word

            #DFS来遍历字典树，按字母顺序从小到大将单词加入res中。
            def getWord(self, k):
                def dfs(node):
                    if dfs.k <= 0: return
                    if node.word:
                        res.append(node.word)
                        dfs.k -= 1
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if not c in node.children:
                            continue
                        dfs(node.children[c])

                res, dfs.k = [], k
                dfs(self.root)
                return res

        #创建桶
        counts = Counter(words)
        bucket = defaultdict(list)
        for word, count in counts.items():
            bucket[count].append(word)
        res = []
        #次数从高到低,最多可能有len(words)次
        for count in range(len(words), 0, -1):
            if not count in bucket:
                continue
            if k <= 0:
                break
            trie = Trie()
            trie.build(bucket[count])
            res += trie.getWord(k)
            k -= len(bucket[count])
        return res



words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
solute = Solution()
res = solute.topKFrequent2(words, k)

