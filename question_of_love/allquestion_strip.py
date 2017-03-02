import sys
import random

all_lines = []

for line in sys.stdin:
	line = line.strip()
	front = line[6:]
	back = front[0:-2]
	print back

