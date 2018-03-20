#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 449_Serialize_and_Deserialize_BST.py
#time_complecity:  
#space_complecity: 
#beats: 

class Codec:
    #前序遍历
    def serialize(self, root):
        def dfs(node):
            if not node:
                stack.append("#")
                return
            stack.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        stack = []
        dfs(root)
        return " ".join(stack)

    def deserialize(self, data):
        def dfs():
            val = stack.pop()
            if val == "#":
                return
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        stack = data.split(" ")
        stack.reverse()
        return dfs()
