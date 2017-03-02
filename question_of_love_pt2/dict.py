import sys

words = dict()

for line in sys.stdin:
	line = line.strip()
	line_words = line.split()
	for word in line_words:
		if word in words:
			words[word] += 1
		else:
			words[word] = 1

sorted_list = sorted( (value, key) for (key, value) in words.items() )

for item in sorted_list: 
	print item
