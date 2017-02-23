import sys

for line in sys.stdin:
	line = line.strip()
	line = line.decode('utf-8','ignore').encode("utf-8")
	if line != '':
		if "From:" in line:
			line = ""
		elif "Date:" in line:
			line = ""
		elif "To:" in line:
			line = ""
		elif "Subject:" in line:
			line = ""
		elif "Sent:" in line:
			line = ""
		elif "Cc:" in line:
			line = ""
		elif "___" in line:
			line = ""
		elif "--" in line:
			line = ""
		elif "==" in line:
			line = ""
		elif "**" in line:
			line = ""
		elif "* " in line:
			line = ""
		elif ">" in line:
			line = ""
		else:
			print line