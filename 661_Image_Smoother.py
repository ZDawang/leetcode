#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 661_Image_Smoother.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #列表生成式的使用。。。
    def imageSmoother(self, M):
        if not M or not M[0]: return M
        h, w = len(M), len(M[0])
        res = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                index = [(x, y) for x in [i - 1, i, i + 1] for y in [j - 1, j, j + 1] if 0 <= x < h if 0 <= y < w]
                res[i][j] = sum([M[x][y] for x, y in index])/len(index)
        return res