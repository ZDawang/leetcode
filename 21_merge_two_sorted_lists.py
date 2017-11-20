#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：
#problem: 21_merge_two_sorted_lists
#time_complecity:  
#space_complecity: 
#beats: 99.56

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	#构造一个函数将列表加进链表中
	def list_append(self, nums):
		head = ListNode(nums[0])
		front = head
		for i in range(1,len(nums)):
			front.next = ListNode(nums[i])
			front = front.next
		return head



class Solution(object):
	def mergeTwoLists(self, l1, l2):
		res = new_l = ListNode(0)
		while l1 and l2:
			(new_l.next, l1, l2) = (l1, l1.next, l2) if l1.val <= l2.val else (l2, l1, l2.next)
			new_l = new_l.next
		new_l.next = l1 if l1 else l2
		return res.next

l1 = [1,3,5,7]
l2 = [2,5,6,7,9,10]

head_l1 = ListNode(1)
head_l1 = head_l1.list_append(l1)


head_l2 = ListNode(2)
head_l2 = head_l2.list_append(l2)

solute = Solution()
res = solute.mergeTwoLists(head_l1, head_l2)

while(res):
	print(res.val)
	res = res.next