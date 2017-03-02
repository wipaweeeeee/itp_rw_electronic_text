import sys
import random

all_lines = []

f = open('topwords.txt', 'r')

for line in f:
	line = line.strip()
	all_lines.append(line)

start = random.sample(all_lines, 1)

for i in range(10):
	the_rest = random.sample(all_lines, i)
	glue = " "
	final_line = glue.join(start) + " " + glue.join(the_rest)
	print final_line
