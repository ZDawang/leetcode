#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-9-
#difficulty degree：
#problem: 141_Linked_List_Cycle.py
#time_complecity:  
#space_complecity: 
#beats: 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #slow，fast
    def hasCycle(self, head):
        if not head.next: return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True

    #slow-fast指针
    #slow每次前进1步，fast每次前进两步
    #若有循环，则会陷入循环，由于slow与fast速度不一样，
    #所以经过确定一段时间后，fast会比slow多走一圈。最终赶上slow
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

    #reverse
    #反转链表，将走过的路径进行反转。
    #若有环，则会从环入口那里回到head处，若没有环，则会到终点处，不会回到head处。
    def hasCycle2(self, head):
        pre, cur = None, head
        while cur:
            pre, cur.next, cur = cur, pre, cur.next
            if cur == head: return True
        return False

