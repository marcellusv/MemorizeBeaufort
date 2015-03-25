#!/usr/bin/python

steps = [0,5,6,8,9,10,11,12,13,14,14,15]

var = 0
for beaufort in range(len(steps) + 1):
	if beaufort == 0:
		print beaufort, '<1'
	elif beaufort + 1 > len(steps):
		print beaufort, '>', var + 1
	else:
		print beaufort, var + 1, '-', var + steps[beaufort]
		var += steps[beaufort]
