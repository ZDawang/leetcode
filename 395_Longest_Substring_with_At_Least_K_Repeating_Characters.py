#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 395_Longest_Substring_with_At_Least_K_Repeating_Characters.py
#time_complecity:  
#space_complecity: 
#beats: 

from collections import defaultdict
from collections import Counter
class Solution(object):
    #分治+滑动窗。可以将问题划分为子问题：只有一个字母出现至少k次的最大长度。只有两个字母。。。
    #26个字母出现至少k次的最大长度。
    def longestSubstring(self, s, k):
        #s为字符串，cnum为字母的个数，k为至少出现次数。
        #滑动窗。
        def helper(s, cNum, k):
            i, j = 0, 0
            #字母的个数计数，以及出现次数多于k的字母个数计数。
            cCnt, kCnt = 0, 0
            maxlength = 0
            times = defaultdict(int)
            while j < len(s):
                #如果出现字母个数小于等于cNum，j++
                if cCnt <= cNum:
                    #更新cCnt，times以及kCnt
                    if times[s[j]] == 0:
                        cCnt += 1
                    times[s[j]] += 1
                    if times[s[j]] == k:
                        kCnt += 1
                    j += 1
                #当字母个数
                else:
                    if times[s[i]] == k:
                        kCnt -= 1
                    times[s[i]] -= 1
                    if times[s[i]] == 0:
                        cCnt -= 1
                    i += 1
                if kCnt == cNum and cCnt == cNum:
                    maxlength = max(maxlength, j - i)
            return maxlength

        return max(helper(s, cNum, k) for cNum in range(1, 27))


    #第一思路：把所有次数小于k的字母全部选出来。因为最终结果中肯定不会有这些字母。
    #所以就可以用这些字母，把字符串分成许多子字符串进行处理。
    #对这些子字符串也做上面的操作。最终找到结果。
    #时间复杂度也为O(n)
    def longestSubstring2(self, s, k):
        #i, j为子字符串的开始与终止位置。
        def helper(s, i, j, k):
            if i > j: return 0
            count = Counter(s[i: j + 1])
            #不满足的字母
            notSatisfy = set([c for c in count if count[c] < k])
            #若所有字母次数都大于等于k
            if len(notSatisfy) == 0:
                return j - i + 1
            #若所有字母次数都小于k
            if len(notSatisfy) == len(count):
                return 0
            #滑动窗，将字符串进行切分。
            start, end = i, i
            res = 0
            while end <= j:
                #根据不满足的字母将s[i: j + 1]进行切分。
                if s[end] in notSatisfy:
                    res = max(res, helper(s, start, end - 1, k))
                    start = end + 1
                end += 1
            #切分的最后一段子字符串。
            res = max(res, helper(s, start, j, k))
            return res
        return helper(s, 0, len(s) - 1, k)


s = "aaabb"
k = 3
solute = Solution()
res = solute.longestSubstring2(s, k)