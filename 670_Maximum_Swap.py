#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-12
#difficulty degree：
#problem: 670_Maximum_Swap.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #分析，结果最大的数，肯定是把最大的数放到首位
    #第一思路：需要找到 两个交换数字的位置。满足以下条件：
    #第一个交换数字前面不可能变的更大。第二个交换数字要尽可能的大，且尽可能的再后面。
    #使用栈。当当前数字比栈顶元素大时，则pop栈顶元素。
    #所以第一个交换的数字，可以确定为被pop的下标最小的位置。
    #第二个元素，则是最后栈中最后一个元素的位置
    def maximumSwap(self, num):
        num = list(str(num))
        stack = []
        i1, i2 = len(num) - 1, len(num) - 1
        maxnum = "0"
        for i, n in enumerate(num):
            if n >= maxnum:
                maxnum, i2 = n, i
            if not stack or n < stack[-1][1]:
                stack.append((i, n))
            else:
                while stack and n > stack[-1][1]:
                    tmpi, tmpn = stack.pop()
                    if tmpi < i1:
                        i1, maxnum, i2 = tmpi, n, i
                stack.append((i, n))
        if i1 < i2:
            num[i1], num[i2] = num[i2], num[i1]
        return int("".join(num))


    #思路：需要找到 两个交换数字的位置。
    #使用栈。当当前数字比栈顶元素大时，则pop栈顶元素。
    #第一个交换的数字，可以确定为被pop的下标最小的位置。也就是尽可能靠前的位置。
    #这样第一个数字就会满足，它之前的数字是最大的数字，比如98636，则第一个数字为6，它前面的98是最大的两个数字。
    #第二个数字的位置，则是栈中第一个数字后面的最大元素的位置。
    #时间复杂度，O(n)

    def maximumSwap2(self, num):
        num = list(str(num))
        #存储下标
        stack = []
        i1 = len(num) - 1
        #寻找第一个数字位置
        for i, n in enumerate(num):
            if not stack or n < num[stack[-1]]:
                stack.append(i)
            else:
                while stack and n > num[stack[-1]]:
                    i1 = min(stack.pop(), i1)
                stack.append(i)

        #寻找第二个数字位置
        #找到i1后面的最大的元素，如果最大的元素有k个，则取最后面的。
        i2, maxnum = len(num) - 1, "-1"
        while stack and stack[-1] > i1:
            tmpi = stack.pop()
            if num[tmpi] > maxnum:
                i2, maxnum = tmpi, num[tmpi]
        #交换
        num[i1], num[i2] = num[i2], num[i1]
        return int("".join(num))

    #难点在于寻找第一个数字的位置，找到第一个数字位置以后，第二个数字就是第一个数字后面最大的数
    #第一个数字需要满足的条件是，它前面的数字是最大的。而且都比它后面的数字大。
    #DP, 时间复杂度O(n)
    #倒序维护一个最大的数字，存储当前位置的后面最大的数字的位置，如果后面有比它大的数字，则说明它有可能是
    #第一个数字。从前向后找，第一个后面有比它大的数字的数字，则是第一个数字。
    def maximumSwap3(self, num):
        num = list(str(num))
        l = len(num)
        maxi = l - 1
        dp = [-1] * l
        #每个位置，存储后面大于等于它的数字的位置
        for i in range(l - 1, -1, -1):
            if num[i] > num[maxi]:
                maxi = i
            dp[i] = maxi
        #找到后面有大于它的数字的位置，交换
        for i in range(l):
            if num[i] != num[dp[i]]:
                num[i], num[dp[i]] = num[dp[i]], num[i]
                break
        return int("".join(num))

            





num = 8998778
solute = Solution()
res = solute.maximumSwap2(num)
print(res)