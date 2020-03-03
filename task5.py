#!/usr/bin/env python
# Input string was left empty for input/output example matching

size = int(input())

matrix = []

i = 0
while i < size:
    matrix.append(list(input().split()))
    i += 1

diag1 = 0
diag2 = 0

for i in range(0, size, 1):
    diag1 += int(matrix[i][i])

for i in range(0, size, 1):
    diag2 += int(matrix[i][size - i - 1])

print(abs(diag1 - diag2))
