#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 640_Solve_the_Equation.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路，对等号两边分别统计x的系数以及常数。然后合并
    def solveEquation(self, equation):
        #统计的思路是直接遍历，用value, symbol表示当前数字的值与符号，遇到x，则把value加入到coe中。
        #否则，加入到const中。
        #helper也可以
        def helper(s):
            coe, const = 0, 0
            value, symbol = 0, 1
            for i, c in enumerate(s):
                if c == "x":
                    #会出现+x，-x这种情况
                    if i == 0 or s[i - 1] == "+":
                        coe += 1
                    elif s[i - 1] == "-":
                        coe -= 1
                    else:
                        coe += value * symbol
                        value, symbol = 0, 1
                #出现符号时，则把当前的数加到const中。
                elif c == "+" or c == "-":
                    const += value * symbol
                    value, symbol = 0, 1 if c == "+" else -1
                else:
                    value = value * 10 + int(c)
            const += value * symbol
            return coe, const
            
        equas = equation.split("=")
        if len(equas) != 2: return "No solution"
        #对两边分别进行处理
        l_coe, l_const = helper(equas[0])
        r_coe, r_const = helper(equas[1])
        if l_coe == r_coe:
            return "Infinite solutions" if l_const == r_const else "No solution"
        return ("x=" + str((r_const - l_const)//(l_coe - r_coe)))

equation = "0x=0"
solute = Solution()
res = solute.solveEquation(equation)