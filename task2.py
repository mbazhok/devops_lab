#!/usr/bin/env python
# Input string was left empty for input/output example matching
initstring = str(input())
if initstring == initstring[::-1]:
	print('yes')
else:
	print('no')