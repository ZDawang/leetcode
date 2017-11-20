#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-20
#difficulty degree：
#problem: 546_Remove_Boxes
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS, TLE,没有剪枝
    def removeBoxes(self, boxes):
        def DFS(boxes, goal, res):
            if not boxes:
                if goal > res[0]: res[0] = goal
            l = len(boxes)
            i = 0
            while(i < l):
                j = i
                while(j < l - 1 and boxes[j] == boxes[j + 1]):
                    j += 1
                    continue
                DFS(boxes[:i] + boxes[j + 1:], goal + (j + 1 - i)**2, res)
                i = j + 1
        res = [0]
        DFS(boxes, 0, res)
        return res[0]

    #DP（DFS+剪枝）
    def removeBoxes2(self, boxes):
        l = len(boxes)
        dp = [[[0] * l for i in range(l)] for j in range(l)]
        def recurse(i, j, k):
            if i > j: return 0
            if dp[i][j][k] > 0: return dp[i][j][k]
            m = i
            while(m + 1 <= j and boxes[m] == boxes[m + 1]):
                m += 1
            i, k = m, k + m - i
            res = (k + 1)**2 + recurse(i + 1, j, 0)

            for m in range(i + 1, j + 1):
                if boxes[i] == boxes[m]:
                    res = max(res, recurse(i + 1, m - 1, 0) + recurse(m, j, k + 1))
            dp[i][j][k] = res
            return res

        return recurse(0, l - 1, 0)


boxes = [1,3,2,2,2,3,4,3,1]
solute = Solution()
res = solute.removeBoxes2(boxes)
