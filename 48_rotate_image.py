#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 48_rotate_image
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        mat_temp = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(matrix[i][j])
            mat_temp.append(temp)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = mat_temp[n - 1 - j][i]


    #第一想法是，图片应该都是0-255的值，用*-1来标记遍历过的数字，结果数组中有负数。。。

    #根据数字原来的坐标可以计算出旋转后新坐标。
    #数字的新坐标(newi, newj) = j, n-1-i
    #数组中每4个数字可以看做一组，这4个数字会顺时针变换位置。
    #所以对n**2/4个数字进行遍历，每个数字所在的一组4个数字进行互换位置即可。
    #最外围一圈4*(n-1)个数字，可以取第一行的数字(去掉第一行最后一个)
    #向里一圈，可以取第二行的数字(去掉第一个以及最后两个)。。。
    #时间复杂度O(n2),空间复杂度O(1)
    def rotate2(self, matrix):
        if not matrix or not matrix[0]: return []
        n = len(matrix)
        #对圈数进行遍历
        for i in range(n//2):
            #对第i圈的四分之一个数进行遍历
            for j in range(i, n-1-i):
                prei, prej, tmp = i, j, matrix[i][j]
                for k in range(4):
                    curi, curj = prej, n - 1 - prei
                    matrix[curi][curj], tmp = tmp, matrix[curi][curj]
                    prei, prej = curi, curj



            




matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16],
]
for i in range(len(matrix)):
   print(matrix[i])
print()
solute = Solution()
solute.rotate2(matrix)

for i in range(len(matrix)):
   print(matrix[i])