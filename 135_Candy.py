#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 135_Candy.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #贪心算法
    #[1,2,3,4,8,8,8,7,6,5,4,3,2,1]
    #当碰到递增的时候，那么糖依次增加
    #当碰到递减的时候，给最后面的一个，前面的依次增加一个
    #当碰到相等的时候，给1个。
    def candy(self, ratings):
        #重新统计后面递减序列的长度,也就是后面要求i位的最小糖数
        def countDecade(ratings, i):
            j, l = i + 1, 0
            while j < len(ratings) and ratings[j] < ratings[j - 1]:
                j += 1
                l += 1
            return l
        start = 0
        mincandy, frontNeed = 0, 1
        behindNeed = countDecade(ratings, 0)

        for i in range(len(ratings)):
            if behindNeed == 0:
                behindNeed = countDecade(ratings, i)

            if behindNeed == 0:
                #若后面跟它相等
                if i != len(ratings) - 1 and ratings[i + 1] == ratings[i]:
                    mincandy += frontNeed
                    frontNeed = 1
                #若后面比它大，则加上当前需要的candy数目，且后面需要的candy数目比当前大
                else:
                    mincandy += frontNeed
                    frontNeed += 1
            #若后面比它小，则加上后面要求它最少的糖数，与前面需要它最小的糖数
            else:
                mincandy += max(behindNeed + 1, frontNeed)
                frontNeed = 1
                behindNeed -= 1
        return mincandy

    #重新构思
    def candy2(self, ratings):
        #重新统计后面递减序列的长度,也就是后面要求i位的最小糖数
        def countDecade(ratings, i):
            j = i + 1
            while j < len(ratings) and ratings[j] < ratings[j - 1]:
                j += 1
            return j - i - 1

        start = 0
        res, frontNeed, behindNeed = 0, 1, 0

        for i in range(len(ratings)):
            #重新统计因为后面需要，当前i的最小糖数
            if behindNeed <= 0: behindNeed = countDecade(ratings, i)
            #前面需要与后面需要的最大值
            res += max(behindNeed + 1, frontNeed)
            #当是递减序列时，那么下一位由于前面需要的最小糖数为1，后面需要的最小糖数-1
            #当不变时，前面需要的最小糖数为1
            if behindNeed != 0 or (i != len(ratings) - 1 and ratings[i + 1] == ratings[i]):
                frontNeed = 1
                behindNeed -= 1
            #当为递增序列时，下一位由于前面需要的最小糖数+1
            else:
                frontNeed += 1
        return res



ratings = [1,2,2,2,2]
solute = Solution()
res = solute.candy(ratings)


    