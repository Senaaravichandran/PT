class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtStart(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def deleteAtstart(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def deleteAtStart(head):
    if head is None:
        print("List is empty")
        return None
    
    new_head = head.next
    del head
    return new_head

def deleteAtEnd(head):
    if head is None:
        print("List is empty")
        return None
    current = head
    while current.next:
        current = current.next
    del current


def traverse(head):
    current = head
    while current:
        print(current.data, end=" => ")
        current = current.next
    print("None")

head = None
head = insertAtStart(head, 4)
head = insertAtStart(head, 3)
head = insertAtStart(head, 2)
head = insertAtStart(head, 1)   

head = deleteAtStart(head)
head = deleteAtEnd(head)