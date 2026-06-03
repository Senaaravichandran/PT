class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self,key):
        if self.head is None:
            return
        current = self.head

        if current.data == key:
            if current.next is None:
                self.head = None
            else:
                self.head = current.next
                self.head.prev = None
            return
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        if current.next:
            current.prev.next = current.next
        
    def display_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Forward: " + " <-> ".join(elements))


    def display_backward(self):
        current = self.head
        if not current:
            print("Backward: List is empty")
            return
            
        while current.next:
            current = current.next
            
    
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("Backward: " + " <-> ".join(elements))


dll = DoublyLinkedList()


dll.append(10)
dll.append(20)
dll.prepend(5)
dll.append(30)

dll.display_forward()   
dll.display_backward()

dll.delete(20)
dll.display_forward()