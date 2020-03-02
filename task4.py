#!/usr/bin/env python
# Input string was left empty for input/output example matching
# Also I included output for numbers that less than 10
num = int(input())
if num < 10:
	print(num+10)
	quit()

guess = []	
for delim in [9,8,7,6,5,4,3,2]:
	while num % delim == 0:
		num	= num / delim
		guess.append(delim)	

if len(guess) < 2:
	print('-1')
	quit()

guess.sort()

res = ''
for i in guess:
	res += str(i)

print(res)