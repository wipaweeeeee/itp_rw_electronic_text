import json

all_title = []
all_word = []
count = {}

with open('Searches/2016-04-01 April 2016 to June 2016.json') as data_file:
	data = json.load(data_file)

	for item in data['event']:
		title = item['query']['query_text'].encode('utf-8')
		if "how " in title:
			all_title.append(title)

	for item in all_title:
		print item
