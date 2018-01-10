#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2018-1
#difficulty degree：
#problem: 462_Minimum_Moves_to_Equal_Array_Elements_II.py
#time_complecity:  
#space_complecity: 
#beats: 
import heapq
class Solution(object):
    #首先我们需要找到那个最终相等的数。
    #考虑1个数的情况，肯定是它自身。
    #考虑两个数的情况，若两个数为a与b，且a<b，则分析可以知道，相等的数取在
    #a与b之间，所需要的步数是相同的，都为(b-c)+(c-a) = b-a
    #所以对于两个数来说，那个相等的数的取值空间为[a, b]
    #对于一个数组来说，我们将最大数与最小数拿出来作为一对，则那个相同的数的取值范围为[最小数，最大数]。
    #将次大数与次小数拿出来作为一对，则那个相同的数的取值范围为[次小数，次大数]，因为
    #[次小数，次大数]与[最小数，最大数]的交集仍为[次小数，次大数]，所以取值范围为[次小数，次大数]
    #如此下去。。。
    #若数组长度为奇数，则最后只剩下一个数(中位数)，因为1个数的情况就是它自身，所以对于数组来说，最终相等的数就是中位数
    #若数组长度为偶数，则最后只剩下两个数(两个中位数)，则最终的取值范围为[较小中位数，较大中位数](包含两个中位数)。
    #所以题目最终变为无序数组寻找中位数。

    #有3种方法：
    #1.直接排序寻找中位数。O(nlogn)
    #2.维护一个大小为n//2的堆。最终堆的最小值为中位数。(O(nlogn))
    #3.使用快排，寻找中位数。(O(n)-O(n2))

    #排序直接找中位数
    def minMoves2(self, nums):
        m = sorted(nums)[len(nums) // 2]
        return sum(abs(num - m) for num in nums)

    #维护一个最小堆来寻找中位数。
    #首先将前半部分加入堆，然后将后半部分依次加入堆中。
    #若加入的数比堆的最小值大，则加入，且堆弹出一个最小值维护长度。
    #若比堆的最小值小，则不加入。
    def minMoves3(self, nums):
        n = len(nums)
        heap = nums[:(n//2+1)]
        heapq.heapify(heap)
        for i in range(n//2+1, n):
            if nums[i] <= heap[0]:
                continue
            heapq.heappush(heap, nums[i])
            heapq.heappop(heap)
        #最终的heap[0]，对于奇数长度的数组来说是中位数
        #对于偶数长度的数组来说，是两个中位数中较大的那个。
        return sum(abs(num - heap[0]) for num in nums)


    #快排寻找中位数。
    #快排的思想是寻找一个轴值，把比轴值小的值放在左边，把比轴值大的值放在右边。
    #因此可以递归寻找中位数。
    #根据轴值的位置，不断选择轴值左边或者右边的数组。最终轴值的位置在n//2处即可。
    #TLE.......，可能是有些例子偏O(N2)了吧。。。
    def minMoves4(self, nums):
        def partion(nums, l, r):
            pivot = nums[l]
            i, j = l, r
            while i < j:
                #右侧扫描，将较小值放到i处
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                #左侧扫描，将较大值放到j处
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            #轴值放在最终位置。
            nums[i] = pivot
            #判断递归哪一部分。
            if i < len(nums)//2:
                return partion(nums, i + 1, r)
            elif i > len(nums)//2:
                return partion(nums, l, i - 1)
            else:
                return nums[i]

        m = partion(nums, 0, len(nums) - 1)
        return sum(abs(num - m) for num in nums)

nums = [1, 2, 3]
solute = Solution()
res = solute.minMoves4(nums)