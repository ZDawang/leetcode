#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-22
#difficulty degree：
#problem: 30_substring_with_concatenation_of_all_words
#time_complecity:  
#space_complecity: 
#beats: 
import collections
class Solution(object):
    # TLE  思想：对每个字符开头向后进行遍历,
    def findSubstring(self, s, words):
        res = []
        d = {}
        rec = {}
        lw = len(words[0])
        if not s or not words:
            return res
        for w in words:
            d[w] = 0
            if w in rec:
                rec[w] += 1
            else:
                rec[w] = 1
        for i in range(len(s) - len(d)*lw + 1):
            for w in d:
                d[w] = 0
            jump = 0
            while (s[i + jump : i + lw + jump]) in d and (rec != d):
                d[s[i + jump : i + lw + jump]] += 1
                if d[s[i + jump : i + lw + jump]] > rec[s[i + jump : i + lw + jump]]:
                    break
                jump += lw
            if d == rec:
                res.append(i)
        return res


    def findSubstring2(self, s, words):
        #滑动窗口，滑动遍历次数：len(words[0])
        ans = []
        d = {}
        l = len(words[0])
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        if not s or not words:
            return res
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans

    #滑动窗口
    #因为词的长度都一样为n。所以先以0为起始点，n为间隔，向右滑动。
    #再以1为起始点，n为间隔向右滑动。。。直到以n-1为起始点，向右滑动。
    def findSubstring3(self, s, words):
        if not words or len(s) < len(words) * len(words[0]):
            return []
        n, res = len(words[0]), []
        counts = collections.Counter(words)
        for i in range(n):
            #窗口的左右边界及窗口内的词
            l, r, d = i, i, {}
            while r < len(s):
                newWord, r = s[r: r+n], r + n
                d[newWord] = d.get(newWord, 0) + 1
                #若新词没在words中出现过
                if not newWord in counts:
                    l, d = r, {}
                #若新词次数过多
                elif d[newWord] > counts[newWord]:
                    while s[l: l+n] != newWord:
                        d[s[l: l+n]], l = d[s[l: l+n]] - 1, l + n
                    d[s[l: l+n]], l = d[s[l: l+n]] - 1, l + n
                #若新词次数不够
                elif d[newWord] < counts[newWord]:
                    continue
                #若新词次数刚好，检查d是否与counts一样
                else:
                    if d == counts:
                        res.append(l)
                        d[s[l: l+n]], l = d[s[l: l+n]] - 1, l + n
        return res




s = "barfoofoobarthefoobarman"


words = ["bar","foo","the"]

solute = Solution()
res = solute.findSubstring2(s, words)

print(res)