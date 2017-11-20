#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 443_String_Compression.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #遍历+计数，分情况写
    def compress(self, chars):
        if not chars: return 0
        prec, count, index = chars[0], 0, 0
        for c in chars:
            if c != prec:
                chars[index] = prec
                index += 1
                if count != 1:
                    l = len(str(count))
                    chars[index: index + l] = str(count)
                    index, count = index + l, 1
            else:
                count += 1
            prec = c
        #最后一个字符
        chars[index] = prec
        index += 1
        if count != 1:
            l = len(str(count))
            chars[index: index + l] = str(count)
            index, count = index + l, 1
        return index

chars = ["a", "b", "b"]
solute = Solution()
res = solute.compress(chars)
print(chars[:res])