import sys
import random

mom_lines = []
all_lines = []
all_love_lines = []
love_lines = []

f = open('mom_question2.txt', 'r')
f2 = open('mom_love2.txt', 'r')
f3 = open('mom_dear.txt', 'r')

for line in f:
	line = line.strip()
	x = line.split()
	all_lines.append(x)

for i in range(10):
	for item in all_lines[i]:
		mom_lines.append(item)

for line in f2:
	line = line.split()
	all_love_lines.append(line)

for line in f3:
	line = line.split()
	all_love_lines.append(line)

for i in range(20):
	for item in all_love_lines[i]:
		love_lines.append(item)

for i in range(4):
	question = random.sample(mom_lines, 5)
	ending = random.sample(love_lines, 3)

	glue = " "
	line_8 = glue.join(question) + " " + glue.join(ending)
	center_align = line_8.center(100)
	print center_align

