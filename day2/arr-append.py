arr=[]
elements = int(input("Enter the no of elements:"))
for x in range(elements):
    data = int(input("enter the elements: "))
    if data % 2 == 0:
        arr.append(data)    
        print(arr)
