class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.nect = new_node


    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end = " ")
                current = current.next
            print()

    def insert_at(self, val, position):
        new_node = Node(val)
        if position==0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count+=1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("None not found")


node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)


node1.next = node2
node2.next = node3
node3.next = node4

print(node1.val)
print(node1.next.val)