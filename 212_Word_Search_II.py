#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 212_Word_Search_II
#time_complecity:  
#space_complecity: 
#beats: 

class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True


class Solution(object):
    def findWords(self, board, words):
        def dfs(i, j, trienode, pre):
            if trienode.end:
                res.add(pre)
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if not visit[i][j] and board[i][j] in trienode.children:
                visit[i][j] = True
                dfs(i + 1, j, trienode.children[board[i][j]], pre + board[i][j])
                dfs(i - 1, j, trienode.children[board[i][j]], pre + board[i][j])
                dfs(i, j + 1, trienode.children[board[i][j]], pre + board[i][j])
                dfs(i, j - 1, trienode.children[board[i][j]], pre + board[i][j])
                visit[i][j] = False
            return

        if not board or not board[0]:
            return []
        trie = Trie()
        for word in words:
            trie.addWord(word)

        m, n = len(board), len(board[0])
        visit = [[False] * n for _ in range(m)]
        res = set()
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, "")
        return list(res)

    

