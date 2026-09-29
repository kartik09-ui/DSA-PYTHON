matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


r = len(matrix)
c = len(matrix[0])

# transpose = [[0] * r for _ in range(0,c)]

for i in range(0,r-1):
    for j in range(i+1,c):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


for i in range(0,r):
    matrix[i].reverse()
        