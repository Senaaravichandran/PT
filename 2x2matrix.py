r = 2
c = 2
mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(input("Enter the data for [{i}][{j}]: "))
    mat.append(row)
print(mat)
for x in mat:
    print(x)