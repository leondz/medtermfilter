#!/usr/bin/env python
# two params: input json filename, serial for output files

import json
import re
import sys

serial = sys.argv[2]

medication_terms = {
	'amisulpride': re.compile(r'\b(amisulpride|Amazeo|Amipride|Amival|Solian|Soltus|Sulpitac|Sulprix)\b',re.I),
	'paliperidone': re.compile(r'\b(paliperidone|Invega)\b',re.I),
	'buprenorphine': re.compile(r'\b(buprenorphine|Subutex|Butrans|Buprenex)\b',re.I),
	'donepezil': re.compile(r'\b(donepezil|Aricept)\b',re.I),
	'memantine': re.compile(r'\b(memantine|Axura|Akatinol|Namenda|Ebixa|Abixa|Memox)\b',re.I),
	'rivastigmine': re.compile(r'\b(rivastigmine|Exelon)\b',re.I),
	'galantamine': re.compile(r'\b(galantamine|Nivalin|Razadyne|Reminyl|Lycoremine)\b',re.I),
	'lurasidone': re.compile(r'\b(lurasidone|Latuda)\b',re.I),
	'brexpiprazole': re.compile(r'\b(brexpiprazole|OPC-34712|OCP34712|OPC 34712)\b',re.I),
	'pimavanserin': re.compile(r'\b(pimavanserin|ACP-103|ACP 103|ACP103|Nuplazid)\b',re.I),
	'vortioxetine': re.compile(r'\b(vortioxetine|Brintellix|Trintellix)\b',re.I),
	'cariprazine': re.compile(r'\b(cariprazine|RGH-188|RGH188|RGH 188)\b',re.I),
	'clozapine': re.compile(r'\b(clozapine|Clozaril|FazaClo|Versacloz|Clopine|Zaponex)\b',re.I),
	'olanzapine': re.compile(r'\b(olanzapine|Zyprexa|Zypadhera|Lanzek)\b',re.I),
	'methadone': re.compile(r'\b(methadone|Symoron|Dolophine|Amidone|Methadose|Physeptone|Heptadon)\b',re.I),
	'risperidone': re.compile(r'\b(risperidone|Risperdal)\b',re.I),
	'citalopram': re.compile(r'\b(citalopram|Celexa|Cipramil)\b',re.I),
	'diazepam': re.compile(r'\b(diazepam|Valium|Diastat|Diastat AcuDial|Zetran)\b',re.I),
	'zopiclone': re.compile(r'\b(zopiclone|Imovane|Zimovane)\b',re.I),
	'promethazine': re.compile(r'\b(promethazine|Phenergan|Promethegan|Romergan|Fargan|Farganesse|Prothiazine|Avomine|Atosil|Receptozine|Lergigan|Sominex)\b',re.I),
	'valproate': re.compile(r'\b(valproate|Epilim|Episenta|Epival|Convulex)\b',re.I),
	'quetiapine': re.compile(r'\b(quetiapine|Seroquel)\b',re.I),
	'lorazepam': re.compile(r'\b(lorazepam|Ativan)\b',re.I),
	'lithium': re.compile(r'\b(lithium|Eskalith|Lithobid|Cibalith S)\b',re.I),
	'aripiprazole': re.compile(r'\b(aripiprazole|Abilify)\b',re.I),
	'mirtazapine': re.compile(r'\b(mirtazapine|Avanza|Axit|Mirtaz|Mirtazon|Remeron|Zispin)\b',re.I),
	'fluoxetine': re.compile(r'\b(fluoxetine|Prozac|Sarafem)\b',re.I),
	'sertraline': re.compile(r'\b(sertraline|Zoloft|Lustral)\b',re.I),
	'venlafaxine': re.compile(r'\b(venlafaxine|Effexor)\b',re.I),
	'haloperidol': re.compile(r'\b(haloperidol|Haldol)\b',re.I)
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
	for med in medication_terms.keys():

		match = re.search(medication_terms[med], record['text'])

		if match:
			destination = "med_"+med

			#print "hit", destination
			
			if destination not in open_files:
				open_files[destination] = open(destination+"_"+serial, 'w')

			open_files[destination].write(line)

	sys.stdout.flush()

for open_file in open_files:
	open_files[open_file].close()