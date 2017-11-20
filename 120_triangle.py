#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-14
#difficulty degree：
#problem: 120_triangle
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #从顶层向下寻找。
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]
        elif len(triangle) == 2:
            return min(triangle[1][0], triangle[1][1]) + triangle[0][0]
        dis_temp = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]
        depth = 2
        #从第三层开始寻找
        for j in range(2, len(triangle)):
            depth += 1
            #从后向前，防止覆盖
            dis_temp += [dis_temp[-1] + triangle[j][-1]]
            for i in range(depth - 2, 0, -1):
                dis_temp[i] = min(dis_temp[i], dis_temp[i - 1]) + triangle[j][i]
            dis_temp[0] += triangle[j][0]
        return min(dis_temp)

triangle = [[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]

solute = Solution()
res = solute.minimumTotal(triangle)
print(res)