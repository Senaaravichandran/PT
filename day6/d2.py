class Node:
    def __init__(self,data):
        self.data = data
        self.data = None
head = Node(0)
head.next=Node(1)
head.next.next=Node(2)

current = head
while current:
    print(current.data,end="=>")
    current = current.next
print("None")