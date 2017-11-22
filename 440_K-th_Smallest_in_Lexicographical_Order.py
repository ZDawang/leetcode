#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 440_K-th_Smallest_in_Lexicographical_Order.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #从最高位按位依次确定
    #将问题统一，从1-n找第k个转为 0到n找第k+1个
    #思路不正确。。因为0的问题
    #比如3058,3后面可以接0到99.没法把后面的数直接代进去。
    def findKthNumber(self, n, k):
        #寻找n里以num开头的有多少个。
        def count(n, num):
            res, power = 0, 1
            while power * 10 < n:
                res, power = res + power, power * 10
            k = n//power
            res = res + power if num < k else (res + n%power + 1 if num == k else res)
            return res

        #因为第一位只能是1开始的，所以用start来控制
        def dfs(n, k, start):
            if k == 0: return ""
            if n[0] == "0":
                return "0" + dfs(n[1:], k-1, 0)
            cnt = 0
            res = ""
            intn = int(n)
            for i in range(start, 10):
                tmp = count(intn, i)
                if cnt + tmp >= k:
                    break
                cnt += tmp
            print(n, k, cnt)
            nextn = n[1:] if str(i) == n[0] else "9" * (len(n) - 1)
            return str(i) + dfs(nextn, k - cnt - 1, 0)

        return int(dfs(str(n), k, 1))


    #别人的代码。。。
    def findKthNumber2(self, n, k):
        result = 1
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result + 1]
            #寻找result到result+1中有多少个数
            while interval[0] <= n:
                count += min(n+1, interval[1]) - interval[0]
                interval = [10*interval[0], 10*interval[1]]
            #如果结果不在result到result+1之中
            if k >= count:
                result += 1
                k -= count
            #如果结果在result到result+1之中
            else:
                result *= 10
                k -= 1
        return result


n, k = 100, 10
solute = Solution()
res = solute.findKthNumber(n, k)





