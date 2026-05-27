numbers=[1,2,3,4,5,6]
remove = [3,4,5]
data=[]
for x in numbers:
    if x not in remove:
        data.append(x)
print(data)