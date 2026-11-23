class Solution:
    def reverse(self, head):
        # code here
        #  Optimal
        if head.next is None:
            return head
        prev = None
        curr = head
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
        return prev
        
        
        # Brute force
        # stack = []
        # temp = head
        # while temp is not None:
        #     stack.append(temp.data)
        #     temp = temp.next
            
        # temp = head
        # while temp is not None:
        #     e = stack.pop()
        #     temp.data = e
        #     temp = temp.next
        # return head
        