#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-7
#difficulty degree ：hard
#problem: 4_midian_of_two_sort_array
#time_complecity:  O(min(m,n))
#space_complecity:  O()
#beats: 60

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # a为短数组，b为长数组
        if len(nums1) < len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1

        l1 = len(a)
        l2 = len(b)

        lc = l1+l2
        if lc < 4 or l1 <= 2:
            c = a + b
            c.sort()
            return c[lc//2] if lc%2 else (c[lc//2 -1] + c[lc//2])/2

        middle_index, odd_or_even = divmod((l1 + l2), 2)
        #将两个数组的首尾各加一个最大数与最小数（这样做所得到的最终结果不变，但可以使循环检测到首尾的值，不然会溢出）
        min_num = min(a[0], b[0])
        max_num = max(a[-1], b[-1])
        a.insert(0, min_num)
        a.append(max_num)
        b.insert(0, min_num)
        b.append(max_num)
        if odd_or_even:
            #当两个数组长度和为奇数时：
            for i in range(1, l1+2):
                print(a[i],b[middle_index + 1 - i],b[middle_index + 2 - i])
                print(b[middle_index + 2 - i],a[i-1],a[i])
                # 寻找a中的一个数，与b的两个数，这三个数的左边数的数量=右边数的数量，检测a是否是这三个数的中位数
                if a[i] <= b[middle_index + 2 - i] and a[i] >= b[middle_index - i + 1]:
                    return a[i]
                # 寻找b中的一个数，与a的两个数，这三个数的左边数的数量=右边数的数量，检测b是否是这三个数的中位数
                elif b[middle_index - i + 2] >= a[i - 1] and b[middle_index - i + 2] <= a[i]:
                    return b[middle_index - i + 2]
                #若都没有找到，则说明a，b没有交叉的数，检测以下情况：a的数是否都小于b的最小值，或b的数是否都小于a的最小值
                elif a[1] >= b[-2]:
                    return b[middle_index + 1]
                elif a[-2] <= b[1]:
                    return b[middle_index - l1 + 1]
        else:
            #当两个数组长度和为偶数时：
            for i in range(1, l1 + 1):
                #寻找6个数（3对），这六个数的左边数的数量=右边数的数量（之所以不寻找2个或4个数的原因，是因为不确定2个中位数在哪个位置）
                l6 = [a[i-1],a[i],a[i+1],b[middle_index - i],b[middle_index - i + 1],b[middle_index - i + 2]]
                #当a的数，在b的3个数之间时，或当b的数，在a的3个数之间时，说明找到中位数
                if ((l6[1] >= l6[3] and l6[1] <= l6[5]) or 
                    (l6[4] >= l6[0] and l6[4] <= l6[2])):
                    #排序（复杂度较高，可优化？）
                    l6.sort()
                    return float(l6[2]+l6[3])/2
            #若没有寻找到，则说明a，b没有交叉的数，检测以下情况：a的数是否都小于b的最小值，或b的数是否都小于a的最小值
            if a[1] >= b[-2]:
                return (b[middle_index] + b[middle_index + 1])/2
            elif a[-2] <= b[1]:
                return (b[middle_index - l1] + b[middle_index - l1 + 1])/2

    #第一种思路，merge+双指针。O(n)
    #第二种思路，二分，查找第k小数。
    def findMedianSortedArrays2(self, nums1, nums2):
        def findKth(A, B, k):
            if not A: return B[k]
            if not B: return A[k]
            ma, mb = len(A)//2, len(B)//2
            #若k比ma+mb大，
            if ma + mb < k:
                #若B的中位数比较小，说明B的前一半肯定不包含第k个数
                #二分法，l=m+1
                if A[ma] > B[mb]:
                    return findKth(A, B[mb + 1:], k - mb - 1)
                else:
                    return findKth(A[ma + 1:], B, k - ma - 1)
            else:
                #若B的中位数比较小，说明A的后一半肯定不包含第k个数
                if A[ma] > B[mb]:
                    return findKth(A[:ma], B, k)
                else:
                    return findKth(A, B[:mb], k)

        l = len(nums1) + len(nums2)
        if l & 1:
            return findKth(nums1, nums2, l // 2)
        else:
            return (findKth(nums1, nums2, l // 2) + findKth(nums1, nums2, l//2 - 1))/2.0






#test
nums1 = [1,1,3,3]
nums2 = [1,1,3,3]

solute = Solution()

res = solute.findMedianSortedArrays(nums1,nums2)
print(res)