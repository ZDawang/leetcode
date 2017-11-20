#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-3-
#difficulty degree：medium
#problem: 19_remove_nth_node_from_end
#time_complecity:  
#space_complecity: 
#beats: 
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

nums = [1,2,3,4,5]
listnode = ListNode(1)
head = listnode.list_append(nums)
#print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val)

class Solution:
	def removeNthFromEnd(self, head, n):
		#去除倒数第n个，也就是正数第length-n个，也就是指针从n到length的距离
		count = remove = head
		for i in range(n):
			count = count.next
		if not count:
			return head.next
		while count.next:
			count = count.next
			remove = remove.next
		remove.next = remove.next.next
		return head

solute = Solution()
res = solute.removeNthFromEnd(head,2)
print(res.val, res.next.val, res.next.next.val, res.next.next.next.val)
