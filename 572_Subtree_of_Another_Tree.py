#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 572_Subtree_of_Another_Tree
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用isroot来标记是否t是否是根节点,耗时有点长
    def isSubtree(self, s, t):
        def dfs(s, t, isroot):
            if (s == None and t != None) or (s != None and t == None):
                return False
            if s == None and t == None:
                return True
            if isroot == 1:
                l, r = dfs(s.left, t, 1), dfs(s.right, t, 1)
                if s.val == t.val:
                    return dfs(s.left, t.left, 0) and dfs(s.right, t.right, 0) or (l or r)
                return l or r
            else:
                if s.val == t.val:
                    return dfs(s.left, t.left, 0) and dfs(s.right, t.right, 0)
                return False
        return dfs(s, t, 1)


    #对每一个节点都进行搜索一次
    def isSubtree(self, s, t):
        def issame(s, t):
            if s == None and t == None: return True
            if not s or not t: return False
            if s.val != t.val:
                return False
            return self.issame(s.left, t.left) and self.issame(s.right, t.right)

        if s == None: return False
        if issame(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    #遍历，in操作可以通过KMP算法，算法复杂度为O(m + n)
    def isSubtree(self, s, t):
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
    
        return convert(t) in convert(s)