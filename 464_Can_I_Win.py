#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-5
#difficulty degree：
#problem: 464_Can_I_Win
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #DFS+memo
    #使用action来代表数字是否使用，每一个bit位代表一个数字。
    def canIWin(self, maxChoosableInteger, desiredTotal):
        def dfs(actions, goal):
            if actions in memo:
                return memo[actions]
            for i in range(maxChoosableInteger, 0, -1):
                a = (1 << (i - 1))
                #当数字没有被选过，且如果选了这个数肯定赢或者选了这个数以后，对方肯定输的时候，可以认为这个action是肯定赢的。
                if actions & a and (goal - i <= 0 or not dfs(actions ^ a, goal - i)):
                    memo[actions] = True
                    return True
            #当没有数字满足肯定能赢的时候。也就是必输
            memo[actions] = False
            return False
        
        total = (maxChoosableInteger * (maxChoosableInteger + 1))//2
        if total < desiredTotal:
            return False
        if total == desiredTotal:
            return maxChoosableInteger % 2 == 1
        
        memo = {}
        return dfs(2**maxChoosableInteger - 1, desiredTotal)