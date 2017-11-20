#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-6
#difficulty degree ：meidum
#problem:2_add_two_numbers
#time_complecity: O(n)
#space_complecity: O(n)
#beats: 40

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		res = []
		carry_bit = 0
		for i in range(min(len(l1), len(l2))):
			if (l1[i]+l2[i] + carry_bit) < 10:
				res.append(l1[i]+l2[i] + carry_bit)
				carry_bit = 0
			else:
				res.append(l1[i]+l2[i] + carry_bit - 10)
				carry_bit = 1
		for i in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
			if len(l2) > len(l1):
				res.append(l2[i])
			else:
				res.append(l1[i])
		return res

l1 = [1,2,3]
l2 = [4,5,6,8]

solute = Solution()

print(solute.addTwoNumbers(l1,l2))



#链表 属性有next，val
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_bit = 0
        root = res = ListNode(0)
        while l1 or l2 or carry_bit:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            res.next = ListNode((v1 + v2 + carry_bit)%10)
            carry_bit = (v1 + v2 + carry_bit)/10
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        return root.next