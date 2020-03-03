#!/usr/bin/env python
# Input string was left empty for input/output example matching
initstring = str(input())
words = initstring.split()

output = ''
for i in words:
    output += i[::-1]
    output += ' '

print(output[:-1])
