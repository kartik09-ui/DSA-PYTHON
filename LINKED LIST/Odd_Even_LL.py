# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        evenHead = head.next
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return head
