import sys
import random

#initialization
all_lines = []

for line in sys.stdin:
	line = line.strip()
	front = line[6:]
	# print front
	back = front[0:-2]
	print back

# poem = random.sample(all_lines, 30)

# for item in all_lines:
# 	print item
