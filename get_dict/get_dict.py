def get_dict(_list):
	count = {}
	for item in _list:
		if item in count:
			count[item] += 1
		else: 
			count[item] = 1

	for key, val in sorted(count.iteritems(), key=lambda x: x[1], reverse=True):
		print key + ": " + str(val)


if __name__ == '__main__':
	import sys
	line = sys.argv[1]
	all_lines = []
	
	line = line.strip()
	all_lines = line.split()
	
	get_dict(all_lines)