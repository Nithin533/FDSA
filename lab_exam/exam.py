class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def beggining(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            
            while temp.next != self.head:
                temp = temp.next
           
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        if not self.head:
            print(" empty.")
            return

        current = self.head
        prev = None

       
        if current.data == key:
            
            if current.next == self.head:
                self.head = None
            else:
                
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                return

        print("Node not found.")
    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("\n")

# Example usage:
cll = CircularLinkedList()
cll.beggining(10)
cll.beggining(20)
cll.beggining(30)
cll.traverse()
cll.delete(10)
cll.traverse()



    

