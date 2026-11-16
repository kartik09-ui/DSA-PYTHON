''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        counter = 0
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != None:
                    slow = slow.next
                    counter+=1
                    if slow == fast:
                        return counter
                        
        return 0