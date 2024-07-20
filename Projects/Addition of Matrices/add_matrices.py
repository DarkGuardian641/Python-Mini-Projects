X = [[5, 2, 3],
     [2, 1, 7],
     [9, 5, 6]]

Y = [[2, 9, 1], 
     [6, 1, 4], 
     [3, 7, 4]]

result = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

for row in range(len(X)):
    for column in range(len(X[0])):
        result[row][column] = X[row][column]+ Y[row][column]

for r in result:
    print(r)
