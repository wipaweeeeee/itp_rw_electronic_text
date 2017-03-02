import sys
import random

#initialization
all_lines = []

for line in sys.stdin:
	line = line.strip()
	if "?" in line:
		all_lines.append(line)

# poem = random.sample(all_lines, 30)

for item in all_lines:
	print item
