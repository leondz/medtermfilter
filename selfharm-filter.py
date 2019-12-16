#!/usr/bin/env python
# two params: input json filename, serial for output files

import json
import re
import sys

serial = sys.argv[2]

self_harm_terms = {
	'self harm': re.compile(r'(\b(selfharm[a-z0-9]*|self harm[a-z0-9]*|self-harm[a-z0-9]*|self_harm[a-z0-9]*|suicid[a-z0-9]*)|#cutting|#selfinjury|#secretsociety123|#selfhate|#blades|#harm|#OD|#overdose)\b',re.I)
}

open_files = {}

for line in open(sys.argv[1], 'r'):

	if not line.strip():
		continue
	try:	
		record = json.loads(line.strip())
	except:
		continue

	if 'lang' in record.keys():
		if record['lang'] != 'en':
			continue

	if 'text' not in record.keys():
		continue

	# there's only one set of "self harm" terms
	match = re.search(self_harm_terms['self harm'], record['text'])

	if match:
		destination = "self_harm"

		#print "hit", destination
		
		if destination not in open_files:
			open_files[destination] = open(destination+"_"+serial, 'w')

		open_files[destination].write(line)



	sys.stdout.flush()

for open_file in open_files:
	open_files[open_file].close()