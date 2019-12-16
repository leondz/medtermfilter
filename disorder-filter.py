#!/usr/bin/env python
# two params: input json filename, serial for output files

import json
import re
import sys

serial = sys.argv[2]

disorder_terms = {
	'add': re.compile(r'(\b(attention deficit|attentiondeficit|attention_deficit|attention-deficit|adhd)|#add)\b',re.I),
	'bipolar': re.compile(r'(\b(bipolar[a-z0-9]*|manic depress[a-z0-9]*|manicdepress[a-z0-9]*|manic-depress[a-z0-9]*|manic_depress[a-z0-9]*)|#biploar)\b',re.I),
	'psychot': re.compile(r'\b(psychos[a-z0-9]*|psychot[a-z0-9]*)\b',re.I),
	'schiz': re.compile(r'(\b(schizophren[a-z0-9]*|schizoaffective|schizo affective|schizo_affective|schizo-affective)|#schizo[a-z0-9]*)\b',re.I),
	'depress': re.compile(r'\b(depress[a-z0-9]*)\b',re.I),
	'ocd': re.compile(r'\b(obsessive compulsive|obsessive-compulsive|obsessive_compulsive|ocd)\b',re.I),
	'autism': re.compile(r'\b([a-z0-9]*autism[a-z0-9]*)\b',re.I),
	'alz': re.compile(r'\b(alzheimer[a-z0-9]*)\b',re.I),
	'dementia': re.compile(r'\b(dementia)\b',re.I),
	'anxiety': re.compile(r'(\b([a-z0-9]*anxiety[a-z0-9]*)|#gad)\b',re.I),
	'mentalhealth': re.compile(r'(\b(#mentalhealth[a-z0-9]*)|#mentalillness|#endstigma|#stigma|#whatstigma|#mhstigma|#stigmahurts)\b',re.I)
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

	#print "searching", record['text']

	for dis in disorder_terms.keys():

		match = re.search(disorder_terms[dis], record['text'])

		if match:
			destination = "dis_"+dis

			#print "hit", destination

			if destination not in open_files:
				open_files[destination] = open(destination+"_"+serial, 'w')

			open_files[destination].write(line)

	sys.stdout.flush()

for open_file in open_files:
	open_files[open_file].close()