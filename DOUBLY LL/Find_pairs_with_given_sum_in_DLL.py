# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        
        # using set SC->O(N)
        # my_set = set()
        # res = []
        # temp = head
        # while temp is not None:
        #     remaining = target - temp.data
        #     if remaining in my_set:
        #         res.append([temp.data,remaining])
        #     else:
        #         my_set.add(temp.data)
        #         temp = temp.next
        # return res
        
        
        # Optimal 
        # Using two pointer becuase distinct and sorted elements
        if head == None:
            return []
        left = head
        right = head
        res = []
        while right.next is not None:
            right = right.next
        while left!=right and left.prev!=right:
            total = left.data + right.data
            if total == target:
                res.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif total < target:
                left = left.next
            else:
                right = right.prev
        return res