import sys 
import random

all_lines = []

for line in sys.stdin:
	if not line.strip():
		continue
	else:
		all_lines.append(line)

random.shuffle(all_lines)
final_lines = random.sample(all_lines, 7)
for item in final_lines:
	print item
