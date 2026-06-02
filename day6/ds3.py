class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtStart(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node  
    return head
def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 1:
        new_node.next = head
        return new

                                  