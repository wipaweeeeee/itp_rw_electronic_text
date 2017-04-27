#markov chain how to from google search, using Allison Parrish's markov module
import markov
import sys

lines = []
in_file = sys.argv[1]

for line in open(in_file):
    line = line.strip()
    lines.append(line)

text = markov.char_level_generate(lines, 4, count=1)
print text

remodel = text[0].replace("how to ", "")
print remodel