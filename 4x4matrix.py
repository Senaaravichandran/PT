mat = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
rows = len(mat)
cols = len(mat[0])
tMat = [[0 for _ in range(rows)] for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        tMat[j][i] = mat[i][j]
for row in tMat:
    for elem in row:
        print(elem, end=' ')
    print()