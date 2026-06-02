class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1=Node(0)
node2=Node(1)
node3=Node(2)
node4=Node(3)

node1.next=node2
node2.next=node3
node3.next=node4

head = node1
current = head
while current:
    print(current.data,"=>")
    current=current.next
print("none")