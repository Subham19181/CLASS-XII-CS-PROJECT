#Program 9

A = [[7,5,4],
     [1,3,2],
     [7,63,2]]

B = [[9,8,5],
     [7,6,6],
     [40,0,91]]

R = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        R[i][j] = A[i][j] + B[i][j]
for r in R:
    print(r)