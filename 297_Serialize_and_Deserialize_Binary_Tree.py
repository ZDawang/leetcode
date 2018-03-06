#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-3
#difficulty degree：
#problem: 297_Serialize_and_Deserialize_Binary_Tree.py
#time_complecity:  
#space_complecity: 
#beats: 

class Codec:
    #前序遍历，用"#"代表空节点，唯一确定一棵树。
    def serialize(self, root):
        def dfs(node):
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        res = []
        dfs(root)
        return " ".join(res)

    #使用前序遍历的方式重新遍历
    def deserialize(self, data):
        def dfs():
            val = stack.pop(0)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node

        stack = data.split(" ")
        return dfs()