#markov chain how to from google search, using Allison Parrish's markov module
import markov
import sys

lines = []
in_file = sys.argv[1]
out_file = sys.argv[2]

with open(out_file, "a") as f:

    for line in open(in_file):
        line = line.strip()
        lines.append(line)

    text = markov.char_level_generate(lines, 4, count=14)
    f.write('\n\n' + '\n'.join(text))
