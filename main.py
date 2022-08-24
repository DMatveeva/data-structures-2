size = 3
matrix = [[0] * size for _ in range(size)]
matrix[1][1] = 2
print(matrix)
print(len(matrix))

nodes_to_check = []
i = 0
while i < len(matrix):
    row = matrix[i]
    print(row)
    print(sum(row))
    if sum(row) > 1:
        nodes_to_check.append(i)
    i += 1
print(nodes_to_check)