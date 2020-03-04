#!/usr/bin/env python
# Input string was left empty for input/output example matching

size = int(input())

matrix = []

for i in range(size):
    matrix.append(list(input().split()))

diag1 = 0
diag2 = 0

for i in range(size):
    diag1 += int(matrix[i][i])

for i in range(size):
    diag2 += int(matrix[i][-1 * (i + 1))

print(abs(diag1 - diag2))
