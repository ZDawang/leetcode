#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-14
#difficulty degree：
#problem: 301_Remove_Invalid_Parentheses
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #因为长度为偶数的括号才能是有效的，所以10的BFS，长度为9的肯定都不是有效的，所以用found来标志即可
    #BFS
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            count = 0
            for c in s:
                if c == "(": count += 1
                if c == ")": count -= 1
                if count < 0: return False
            return count == 0

        queue = [s]
        res = []
        visit = set()
        found = False
        while queue:
            s = queue.pop(0)
            if isvalid(s):
                res.append(s)
                found = True
            if found:
                continue
            for i in range(len(s)):
                if s[i] == "(" or s[i] == ")":
                    t = s[:i] + s[i + 1:]
                    if t in visit:
                        continue
                    queue.append(t)
                    visit.add(t)
        return res

    #DFS, TLE, 没有剪枝
    def __init__(self):
        self.lres = 0
        self.res = set()
    def removeInvalidParentheses2(self, s):
        def isvalid(s):
            count = 0
            for c in s:
                if c == "(": count += 1
                if c == ")": count -= 1
                if count < 0: return False
            return count == 0

        def dfs(s):
            l = len(s)
            if l < self.lres: return
            if isvalid(s):
                if l == self.lres:
                    self.res.add(s)
                else:
                    self.lres = l
                    self.res = set([s])
                return
            for i in range(l):
                if s[i] == "(" or s[i] == ")":
                    dfs(s[:i] + s[i + 1:])
            return
        dfs(s)
        return list(self.res)



s = "()(((((((()"
solute = Solution()
res = solute.removeInvalidParentheses2(s)


