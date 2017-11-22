#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3- 8
#difficulty degree：medium
#problem: 6_zigzag_conversion
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #将结果的每一行放入一个字符串中，最终将这些字符串拼接即可
    #direction代表方向，向上或者向下。k为第几行
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        zip_data = []
        direction, k = -1, numRows - 2
        for i in range(len(s)):
            #先把各行的第一个字母写入到zip_data中
            if i < numRows:
                zip_data.append(s[i])
            #把各行的其它字母按规律加入
            else:
                zip_data[k] += s[i]
                #调转方向
                if k == 0 or k == numRows -1:
                    direction *= -1
                k = k + direction
        return "".join(zip_data)

s = "abcdefghijklmn"

solute = Solution()

res = solute.convert(s, 4)
print (res)