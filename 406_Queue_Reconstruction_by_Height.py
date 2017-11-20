#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 406_Queue_Reconstruction_by_Height.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #将people按出现次数与身高排序。使用贪心法依次插入。
    #先将次数低的插入，插入时尽可能的向后插入，以免影响到其它的元素。
    #时间复杂度，O(n2)
    def reconstructQueue(self, people):
        people.sort(key = lambda x: (x[1], x[0]))
        res = []
        for p in people:
            count, index = 0, 0
            while count <= p[1] and index < len(res):
                if res[index][0] >= p[0]:
                    count += 1
                index += 1
            res.insert(index if count <= p[1] else index - 1, p)
        return res

    #换一个思路
    #先将高个子的插入，低个子的就可以直接使用p[1]进行插入，因为高个子的位置都已经确定了
    #O(nlogn)
    def reconstructQueue2(self, people):
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
solute = Solution()
res = solute.reconstructQueue(people)