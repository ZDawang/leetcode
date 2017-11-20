#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-21
#difficulty degree：
#problem: 500_Keyboard_Row
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def findWords(self, words):
        d = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
            'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
            'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
        res = []
        for word in words:
            flag = 1
            label = d[word[0].lower()]
            for w in word:
                if d[w.lower()] != label:
                    flag = 0
                    break
            if flag: res.append(word)
        return res

words = ["Hello", "Alaska", "Dad", "Peace"]
solute = Solution()
res = solute.findWords(words)
print(res)