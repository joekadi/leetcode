#https://leetcode.com/problems/reverse-linked-list/
from tkinter.tix import ListNoteBook
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
