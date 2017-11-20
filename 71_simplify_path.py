#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 71_simplify_path
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def simplifyPath(self, path):
        place = [p for p in path.split('/') if p != '.' and p!= '']
        stack = []
        for p in place:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)