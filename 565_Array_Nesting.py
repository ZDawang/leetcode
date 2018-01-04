#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 565_Array_Nesting
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #可以认为，nums中会分成许多个cycle，DFS即可。将遍历过的都标-1
    def arrayNesting(self, nums):
        res = 0
        for i, num in enumerate(nums):
            if num == -1:
                continue
            start, tmp = i, 1
            while nums[start] != i and nums[start] != -1:
                nums[start], start = -1, nums[start]
                tmp += 1
            nums[start] = -1
            res = max(res, tmp)
        return res

    #并查集
    #并查集变种。若uf[x]小于0，则说明x是根节点。且-uf[x]是集合中的个数。
    #若uf[x]大于0，则x指向uf[x]。
    #这种并查集可以得到集合的个数，以及每个集合中的个数。比较方便。
    def arrayNesting2(self, nums):
        def find(x):
            if uf[x] < 0: return x
            uf[x] = find(uf[x])
            return uf[x]
            
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return 
            #x中元素较少，将x指向y
            if uf[x] > uf[y]:
                uf[y] += uf[x]
                uf[x] = y
            else:
                uf[x] += uf[y]
                uf[y] = x

        uf = [-1 for i in range(len(nums))]
        for i, num in enumerate(nums):
            union(i, num)
        return -max(uf, key = lambda x: -x)




nums = [5,4,0,3,1,6,2]
solute = Solution()
res = solute.arrayNesting2(nums)