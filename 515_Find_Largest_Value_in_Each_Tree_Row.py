#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-4
#difficulty degree：
#problem: 515_Find_Largest_Value_in_Each_Tree_Row
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #BFS，用"#"来分割层。
    def largestValues(self, root):
        if not root: return []
        res = []
        queue = [root, "#"]
        maxnum = root.val
        while queue:
            root = queue.pop(0)
            #当前层结束
            if root == "#":
                if queue: queue.append("#")
                res.append(maxnum)
                maxnum = float("-inf")
                continue
            maxnum = max(maxnum, root.val)
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
        return res

    #DFS,用h表示node的深度，对同一深度的节点选择最大的值。
    def largestValues2(self, root):
        def dfs(node, h):
            if not node: return
            if h >= len(res):
                res.append(node.val)
            else:
                res[h] = max(res[h], node.val)
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)

        res = []
        dfs(root, 0)
        return res

