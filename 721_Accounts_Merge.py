#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 721_Accounts_Merge.py
#time_complecity:  
#space_complecity: 
#beats: 
from collections import defaultdict
class Solution(object):
    #并查集
    #使用uf来代表uf表，name用来查找邮箱的名字，emailSet用来代表根节点对应的集合里面的所有元素。
    def accountsMerge(self, accounts):
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return False
            uf[x] = y
            emailSet[y].update(emailSet.pop(x))
            return True

        #初始化uf表以及name表以及emailSet
        uf, name, emailSet = {}, {}, defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                uf[account[i]] = account[i]
                name[account[i]] = account[0]
                emailSet[account[i]].add(account[i])
        #融合
        for account in accounts:
            for i in range(1, len(account)):
                union(account[i], account[1])

        res = []
        for email in emailSet:
            res.append([name[email]] + sorted(list(emailSet[email])))
        return res

accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
solute = Solution()
res = solute.accountsMerge(accounts)