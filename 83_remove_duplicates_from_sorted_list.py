#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data:2017-4-
#difficulty degree：
#problem: 83_remove_duplicates_from_sorted_list
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
    def show(self):
        print(self.val)


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return
        start = res = head
        while(head.next):
            if head.val == head.next.val:
                head = head.next
            else:
                start.next = head.next
                start = start.next
                head = head.next
        start.next = None
        return res

l1 = [1,1,2,5]

head = ListNode(1)
head = head.list_append(l1)
solute = Solution()
res = solute.deleteDuplicates(head)

while(res):
    print(res.val)
    res = res.next
