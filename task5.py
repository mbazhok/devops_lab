#!/usr/bin/env python
# Input string was left empty for input/output example matching

size = int(input())

matrix = []

for i in range(size):
    matrix.append(list(input().split()))

dg1 = 0
dg2 = 0

for i in range(size):
    dg1 += int(matrix[i][i])

for i in range(size):
    dg2 += int(matrix[i][-1 * (i + 1)])

print(abs(dg1 - dg2))
