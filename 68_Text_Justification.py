#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 68_Text_Justification.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用stack存储当前需要添加到结果中的字符，使用length来记录当前所需要的长度。
    #当长度大于maxWidth时，添加空格，把结果存放到res中
    def fullJustify(self, words, maxWidth):
        res = []
        stack = []
        length = -1
        for word in words:
            #有空格, 所以长度要多+1
            length += len(word) + 1
            #当长度超出时，将stack中的字符都放入结果中
            if length > maxWidth:
                length = length - len(word) - 1
                totalspacelen = maxWidth - length
                #每个字符间需要加的空格数量
                if len(stack) > 1:
                    spacelen, extralen = divmod(totalspacelen, (len(stack) - 1))
                    linestr = stack[0]
                    for i in range(1, len(stack)):
                        if i <= extralen:
                            linestr = linestr + " " * (spacelen + 2) + stack[i]
                        else:
                            linestr = linestr + " " * (spacelen + 1) + stack[i]
                else:
                    linestr = stack[0] + " " * (maxWidth - length)
                res.append(linestr)
                length = len(word)
                stack = [word]
            else:
                stack.append(word)
        res.append(" ".join(stack) + " " * (maxWidth - length))
        return res

words = ["a","b","c","d","e"]
maxWidth = 1
solute = Solution()
res = solute.fullJustify(words, maxWidth)


