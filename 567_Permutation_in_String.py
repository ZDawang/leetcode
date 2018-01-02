#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 567_Permutation_in_String
#time_complecity:  
#space_complecity: 
#beats: 

from collections import Counter, defaultdict
class Solution(object):
    #双指针
    #统计s1中的字母。对于s2中的子序列，若没有在s1中出现过，则start=end+1
    #若出现次数大于s1中的次数，则递增start，直到次数等于s1中的次数。
    #判断count1与count2是否相同或者end-start+1是否与s1的长度相同。
    def checkInclusion(self, s1, s2):
        if not s1: return True
        if not s2 or len(s2) < len(s1): return False
        count1 = Counter(s1)
        start = 0
        count2 = defaultdict(int)
        for end, c in enumerate(s2):
            if not c in count1:
                start = end + 1
                count2.clear()
                continue
            while count2[c] >= count1[c]:
                count2[s2[start]] -= 1
                start += 1
            count2[c] += 1
            if end - start + 1 == len(s1):
                return True
        return False