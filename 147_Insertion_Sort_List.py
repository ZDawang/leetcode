#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 147_Insertion_Sort_List.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #插入排序。对于cur指针，从head开始找比cur大的第一个节点，然后插入
    #cur是需要进行插入操作的节点。pre是cur的前一个节点。
    #需要插入到preinsert到insert之间。
    def insertionSortList(self, head):
        if not head or not head.next: return head
        pre, cur = head, head.next
        while cur:
            if cur.val >= pre.val:
                cur, pre = cur.next, cur
                continue
            else:
                #插入
                insert, preinsert = head, None
                while insert.val < cur.val:
                    insert, preinsert = insert.next, insert
                #插入头部
                pre.next = cur.next
                if not preinsert:
                    cur.next = insert
                    head = cur
                else:
                    preinsert.next = cur
                    cur.next = insert
                cur = pre.next
        return head