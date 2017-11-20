#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 501_Find_Mode_in_Binary_Search_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #先序遍历，用maxtimes来存储最大结果
    def findMode(self, root):
        if not root: return []
        res = []
        stack = []
        maxtime, curtime = 0, 0
        curnum = root.val
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val == curnum:
                curtime += 1
            else:
                if curtime > maxtime:
                    res = [curnum]
                if curtime == maxtime:
                    res.append(curnum)
                maxtime = max(maxtime, curtime)
                curnum, curtime = root.val, 1
            root = root.right
        #处理最后一个值
        if curtime > maxtime:
            res = [curnum]
        if curtime == maxtime:
            res.append(curnum)
        return res
