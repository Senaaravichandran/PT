t = int(input())

for _ in range(t):
    temp = input().split()
    n = int(temp[0])
    k = int(temp[1])

    values = input().split()

    stack = []

    for i in range(n):
        stack.append(int(values[i]))

    k = k % n

    rotated = []

    # Add elements from k to n-1
    for i in range(k, n):
        rotated.append(stack[i])

    # Add first k elements
    for i in range(k):
        rotated.append(stack[i])

    for i in range(n):
        print(rotated[i], end=" ")
    print()
