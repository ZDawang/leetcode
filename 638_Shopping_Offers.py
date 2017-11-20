#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-8-25
#difficulty degree：
#problem: 638_Shopping_Offers
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用字典来记录所有可能组合结果
    def shoppingOffers(self, price, special, needs):
        #判断是否超过个数
        def isExceed(l, list1, list2):
            for i in range(l):
                if list1[i] > list2[i]:
                    return True
            return False

        maxprice = float("inf")
        l = len(price)
        d = {(0, ) * l: 0}
        #列举所有可能结果
        for spe in special:
            newd = d.copy()
            for key in d:
                for i in range(6):
                    newkey = [0]*l
                    for j in range(l):
                        newkey[j] = key[j] + (i + 1)*spe[j]
                    if isExceed(l, newkey, needs):
                        break
                    newkey = tuple(newkey)
                    newd[newkey] = min(newd.get(newkey, maxprice), d[key] + (i + 1) * spe[-1])
            d = newd

        #得到最小结果
        res = maxprice
        for key in d:
            keyprice = d[key]
            for i in range(l):
                keyprice += (needs[i] - key[i]) * price[i]
            res = min(res, keyprice)
        return res

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]

solute = Solution()
res = solute.shoppingOffers(price, special, needs)


