#https://leetcode.com/problems/linked-list-cycle/
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited_vals = []
    
        while head:
            if head in visited_vals:
                return True
            else:
                visited_vals.append(head)
            head = head.next
            