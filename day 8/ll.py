class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    def insert_at_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_after_node(self, prev_node_data, data):
        curr = self.head
        while curr and curr.data != prev_node_data:
            curr = curr.next
        if not curr:
            return
        new_node = Node(data)
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    def delete_at_first(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def delete_after_node(self, prev_node_data):
        curr = self.head
        while curr and curr.data != prev_node_data:
            curr = curr.next
        if not curr or not curr.next:
            return
        node_to_delete = curr.next
        curr.next = node_to_delete.next
        if node_to_delete.next:
            node_to_delete.next.prev = curr