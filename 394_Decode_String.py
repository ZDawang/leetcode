#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 394_Decode_String.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def decodeString(self, s):
        res = ""
        countstack = []
        resstack = []
        i = 0
        while i < len(s):
            #当为数字时，先存起来
            if s[i].isdigit():
                count = 0
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
                countstack.append(count)
            #当[开始时，把前面的结果先放起来，重新做一个结果
            elif s[i] == "[":
                resstack.append(res)
                res = ""
                i += 1
            #当]结束时，res = 前面的结果+当前的结果*重复次数
            elif s[i] == "]":
                res = resstack.pop() + res * countstack.pop()
                i += 1
            else:
                res = res + s[i]
                i +=1
        return res


