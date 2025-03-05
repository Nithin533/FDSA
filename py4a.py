class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        
        new_node = Node(data)
        if not self.head:
            
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def search(self, data):
        
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  


linked_list = list()


linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Linked list after appending ")
linked_list.display()


print("Searching for node with value 20:", linked_list.search(20))  
print("Searching for node with value 40:", linked_list.search(40))  

