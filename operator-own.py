numbers=[1,2,3,4,5,6]
remove = [7,8,6]
data = numbers+remove
print(data)
for i in list(numbers):
    for j in list(remove):
        if (i == j):
            remove.remove(j)
            print(numbers + remove)