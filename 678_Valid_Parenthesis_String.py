#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-11-29
#difficulty degree：
#problem: 678_Valid_Parenthesis_String
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #从左到右，保证")"数量小于等于"("，而且"*"够用
    #从右到左，保证"("数量小于等于")"，而且"*"够用
    #来回两遍的作用是，第一遍是为了防止"*"不够转换成"("。第二遍是防止"*"不够转换成"("
    def checkValidString(self, s):
        def check(s, p1, p2):
            cnt1, cnt2, star = 0, 0, 0
            for c in s:
                if c == p1:
                    cnt1 += 1
                elif c == p2:
                    cnt2 += 1
                else:
                    star += 1
                if cnt2 > cnt1 + star:
                    return False
            return cnt2 - cnt1 <= star

        return check(s, "(", ")") and check(s[::-1], ")", "(")

    #每次加一个"*",都有三种可能性。
    #使用左括号数量-右括号数量来记录结果。
    #使用low，high来记录左括号数量-右括号数量的范围。
    def checkValidString2(self, s):
        low, high = 0, 0
        for c in s:
            if c == "(":
                low, high = low + 1, high + 1
            elif c == ")":
                low = max(low - 1, 0)
                high = high - 1
                if high < 0: return False
            else:
                low = max(low - 1, 0)
                high = high + 1
        return low == 0

    #两个栈,一个栈存储左括号，一个栈存储"*"
    #思想是，先把右括号满足，再把左括号满足。
    #所以出现右括号时，尽可能的用左括号来填。
    #最终剩下的左括号跟"*"，此时是需要把剩下的左括号匹配。所以"*"需要在左括号右边。
    def checkValidString3(self, s):
        left, star = [], []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left



