class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertb(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def inserte(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current:
            if current.data == data:
                if prev:  # not the first node
                    prev.next = current.next
                else:  # if it's the head node
                    self.head = current.next
                current = current.next  # Continue to check for other occurrences
            else:
                prev = current
                current = current.next
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()
linked_list = LinkedList() 

linked_list.insertb(10) 
linked_list.insertb(20)
linked_list.insertb(30)
print("Linked list after inserting 10 ,20, 30 at the beginning:") 
linked_list.traverse() 
linked_list.inserte(5)
linked_list.inserte(10)
linked_list.inserte(15) 
linked_list.inserte(20) 
print("\nLinked list after inserting 5, 10 , 15, 20  at the end:")
linked_list.traverse() 

linked_list.delete(20) 
print("\nLinked list after deleting node with data 20:") 
linked_list.traverse() 

print("\nTraversing the linked list:") 
linked_list.traverse() 


