#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 733_Flood_Fill.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS + visit
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j, preColor, newColor):
            #若越界
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            #若已访问过或者颜色不同
            if (i*n + j) in visit or image[i][j] != preColor:
                return
            image[i][j] = newColor
            visit.add(i * n + j)
            dfs(i + 1, j, preColor, newColor)
            dfs(i - 1, j, preColor, newColor)
            dfs(i, j + 1, preColor, newColor)
            dfs(i, j - 1, preColor, newColor)

        if not image or not image[0]:
            return []
        m, n = len(image), len(image[0])
        visit = set()
        dfs(sr, sc, image[sr][sc], newColor)
        return image