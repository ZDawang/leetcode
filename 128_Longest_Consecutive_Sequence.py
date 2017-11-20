#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-15
#difficulty degree：
#problem: 128_Longest_Consecutive_Sequence
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #TLE
    def longestConsecutive2(self, nums):
        if not nums:
            return 0
        d = {}
        #寻找当前数的连续数是否在字典中
        for num in nums:
            if num in d:
                continue
            d[num] = d.get(num + 1, 0) + d.get(num - 1, 0) + 1
            i = 1
            while(1):
                if num + i in d:
                    d[num + i] = d[num]
                    i += 1
                else:
                    break
            j = 1
            while(1):
                if num - j in d:
                    d[num - j] = d[num]
                    j += 1
                else:
                    break
            print(d)
        return max(d.values())

    def longestConsecutive(self, nums):
        #创建字典，将寻找过的数字都标为2，后面不做寻找
        d = {}
        res = 0
        for num in nums:
            d[num] = 1
        for element in d:
            if d[element] == 2:
                continue
            seqnum = 1
            temp = element + 1
            while(temp in d):
                seqnum += 1
                d[temp] = 2
                temp += 1
            temp = element - 1
            while(temp in d):
                seqnum += 1
                d[temp] = 2
                temp -= 1
            res = max(res, seqnum)
        return res

    #并查集
    def longestConsecutive2(self, nums):
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return
            uf[x] = y
            d[x], d[y] = 0, d[x] + d[y]
        
        #用来记录各个集合内元素的数量
        d = {num: 1 for num in nums}
        uf = {num: num for num in nums}
        #对于数组中的数，与比它大一的数进行融合
        for num in nums:
            if num + 1 in d:
                union(num, num + 1)
        return max(d.values() or [0])



nums = [1,2,0,1]
solute = Solution()
res = solute.longestConsecutive(nums)
print(res)