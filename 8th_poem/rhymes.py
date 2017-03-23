import sys
import random
import pronouncing

all_words = []
glue = " "

for line in sys.stdin:
	line = line.strip()
	for word in line.split():
		all_words.append(word)

line_1 = random.sample(all_words, 8)
line_1_rhymes = pronouncing.rhymes(line_1[7])

intercept = set(line_1_rhymes).intersection(all_words)

if len(intercept) > 1:
	lastword = random.sample(intercept,1)
else:
	lastword = intercept

line_2_1 = random.sample(all_words, 2)
line_2_2 = random.sample(all_words, 5)
line_2_full = line_2_1 + lastword + line_2_2
line_2_rhymes = pronouncing.rhymes(line_2_full[7])

line_2_intercept = set(line_2_rhymes).intersection(all_words)

if len(line_2_intercept) > 1:
	line_3_lastword = random.sample(line_2_intercept, 1)
else:
	line_3_lastword = line_2_intercept

line_3 = random.sample(all_words, 7)
line_3_full = line_3 + line_3_lastword
line_3_rhymes = pronouncing.rhymes(line_3_full[7])

line_3_intercept = set(line_3_rhymes).intersection(all_words)

if len(line_3_intercept) > 1:
	line_4_lastword = random.sample(line_2_intercept, 1)
else:
	line_4_lastword = line_3_intercept

line_4_1 = random.sample(all_words, 2)
line_4_2 = random.sample(all_words, 5)
line_4_full = line_4_1 + line_4_lastword + line_4_2

print glue.join(line_1)
print glue.join(line_2_full)
print glue.join(line_3_full)
print glue.join(line_4_full)


