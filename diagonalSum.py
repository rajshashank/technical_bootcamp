def diagonal_sums(matrix):
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]

    return primary_diagonal_sum, secondary_diagonal_sum

matrix = [
    [1, 2, 4],
    [6, 5, 6],
    [7, 8, 9]
]

primary_sum, secondary_sum = diagonal_sums(matrix)
print("Sum of primary diagonals is:", primary_sum)
print("Sum of secondary diagonals is:", secondary_sum)
