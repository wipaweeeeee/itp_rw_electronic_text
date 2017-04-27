#markov chain how to from google search, using Allison Parrish's markov module
import markov
import sys
import random

lines = []
courses = []
howtos = []
image_set = []
out_file = sys.argv[1]

with open('itp_course.txt') as course:
	for line in course:
		line = line.strip()
		courses.append(line)
	# print courses

with open('howto.txt') as how:
	for line in how:
		line = line.strip()
		howtos.append(line)
	how_title = markov.char_level_generate(howtos, 4, count=1)
	for line in how_title:
		title = line.replace("how to ", "")

with open('images.txt') as images:
	for line in images:
		line = line.strip()
		image_set.append(line)


with open(out_file, "a") as f:
    text = markov.char_level_generate(courses, 13, count=2)
    image = random.choice(image_set)
    f.write(title + '\n' + image + '\n' + '\n'.join(text) + '\n\n')
