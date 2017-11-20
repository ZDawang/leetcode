#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-5
#difficulty degree：
#problem: 652_Find_Duplicate_Subtrees
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #最基本思路，将所有点都比较一遍 O(n2*m), TLE
    def findDuplicateSubtrees(self, root):
        def issame(s, t):
            if s == None and t == None: return True
            if not s or not t: return False
            if s.val != t.val:
                return False
            return issame(s.left, t.left) and issame(s.right, t.right)

        if not root: return []
        stack = []
        nodelist = []
        donenode = set()
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            for node in nodelist:
                if issame(node, root):
                    if node in donenode:
                        donenode.add(root)
                        break
                    res.append(node)
                    donenode.add(root)
                    donenode.add(node)
            nodelist.append(root)
            root = root.right
        return res

    #与572题相同，利用前向遍历


    #首先找出所有节点作为根节点的遍历结果，最主要的是这个遍历的结果要与树的结构是一一对应的关系，无论使用哪种遍历方式都无所谓。
    #然后查看这些遍历结果中有没有相同的，有的话则说明树结构相同，拿出来加入最终结果。
    def findDuplicateSubtrees2(self, root):
        def preorder(root, d):
            if not root: return "&"
            #加入"^" 以及 "&" 是为了使order与树的结构有唯一的对应关系。
            order = "^" + preorder(root.left, d) + str(root.val)  + preorder(root.right, d) + "^"
            if order in d:
                d[order] = root
            else:
                d[order] = 0
            return order

        d, res = {}, []
        preorder(root, d)
        for key in d:
            if d[key] != 0: res.append(d[key])
        return res

