import csv
import os
from re import match
import xml.etree.ElementTree as ET

''' For getting default values from database schema '''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riboswitches_app.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from database.models import *


def readAttrb(value, default = None):
	try:
		value = int(value)
	except ValueError:
		pass

	default = value if default == None else default

	if (isinstance(default, int) and isinstance(value, str)) or value == "": # If user typed in wrong integer, ex. "135r6" or left empty string
		return(default)
	elif isinstance(default, str) and isinstance(value, str):
		return(value.strip())
	elif isinstance(default, int) and isinstance(value, int):
		return(int(value))


def loadDataToDictionary(fileName, isResult = False):
	# If result, then redirect to proper filepath
	if isResult == True:
		fileName = "../Riboswitches/Results/" + fileName

	'''
	Dictionary that represents all possible data which can be obtained for a single riboswitch record:
	'''
	d = {
			# Record #
		'operon_genes':					Record._meta.get_field('genes_under_operon_regulation').get_default(), # [ Array ]
		'effect':					Record._meta.get_field('effect').get_default(),
		'mechanism':					Record._meta.get_field('mechanism').get_default(),
		'confirmation':					Record._meta.get_field('mechanism_confirmation').get_default(),
		'sequence':					Record._meta.get_field('sequence').get_default(),						
		# ''' Linked with Gene '''	#
		# ''' Linked with RiboFamily '''#
		# ''' Linked with Article '''	#

			# Aptamer #
		'aptamer_start':				Position._meta.get_field('start').get_default(),				# [ Array ]
		'aptamer_end':					Position._meta.get_field('end').get_default(),					# [ Array ]
		'aptamer_score':				Position._meta.get_field('score').get_default(),				# [ Array ]
		# ''' Linked with Structure2D '''#

			# RiboClass #
		'class_name':					RiboClass._meta.get_field('name').get_default(),
		'class_description':				RiboClass._meta.get_field('description').get_default(),
		'class_alignment':				RiboClass._meta.get_field('alignment').get_default(),

			# RiboFamily #
		'family_name':					RiboFamily._meta.get_field('name').get_default(),
		'family_description':				RiboFamily._meta.get_field('description').get_default(),
		'family_alignment':				RiboFamily._meta.get_field('alignment').get_default(),

			# Gene #
		'gene_name':					Gene._meta.get_field('name').get_default(),
		'locus_tag':					Gene._meta.get_field('locus_tag').get_default(),
		'gene_start':					Position._meta.get_field('start').get_default(),
		'gene_end':					Position._meta.get_field('end').get_default(),
		'location':					Position._meta.get_field('location').get_default(),
		'strand':					Position._meta.get_field('strand').get_default(),
		# ''' Linked with Organism '''	#

			# Organism #
		'scientific_name':				Organism._meta.get_field('scientific_name').get_default(),
		'common_name':					Organism._meta.get_field('common_name').get_default(),
		'organism_accession_number':			Organism._meta.get_field('accession_number').get_default(),
		'build_id':					Organism._meta.get_field('build_id').get_default(),
		# ''' Linked with Taxonomy ''' #

			# Taxonomy #
		'taxonomy_name':				Taxonomy._meta.get_field('name').get_default(),					# [ Array ]
		'taxonomy_id':					Taxonomy._meta.get_field('taxonomy_id').get_default(),				# [ Array ]

			# LigandClass #
		'ligand_class_name':				LigandClass._meta.get_field('name').get_default(),				# [ Array ]
		'ligand_class_description':			LigandClass._meta.get_field('description').get_default(),			# [ Array ]

			# Ligand #
		'ligand_name':					Ligand._meta.get_field('name').get_default(),					# [ Array ]
		'ligand_description':				Ligand._meta.get_field('description').get_default(),				# [ Array ]
		'image_name':					Ligand._meta.get_field('image_name').get_default(),				# [ Array ]
		# ''' Linked with LigandClass '''#

			# Structure 2D #
		'without_ligand':				Structure2D._meta.get_field('without_ligand').get_default(),			# [ Array ]
		'with_ligand':					Structure2D._meta.get_field('with_ligand').get_default(),			# [ Array ]
		'predicted':					Structure2D._meta.get_field('predicted').get_default(),				# [ Array ]

			# Terminator #
		'terminator_start':				Position._meta.get_field('start').get_default(),
		'terminator_end':				Position._meta.get_field('end').get_default(),
		'terminator_score':				Position._meta.get_field('score').get_default(),

			# Promoter # 
		'promoter_start':				Position._meta.get_field('start').get_default(),
		'promoter_end':					Position._meta.get_field('end').get_default(),
		'promoter_score':				Position._meta.get_field('score').get_default(),

			# Shine-Dalgarno # 
		'sd_start':					Position._meta.get_field('start').get_default(),
		'sd_end':					Position._meta.get_field('end').get_default(),
		'sd_score':					Position._meta.get_field('score').get_default(),

			# Articles #
		'articles':					Record._meta.get_field('articles').get_default(),				# [ Array ]
			
			# Structures 3D #
		'structure_3d':					Structure3D._meta.get_field('pdbid').get_default(),				# [ Array ]
	}

	extension = fileName.split('.')[-1]
	if extension == 'csv' or 'tsv':
		return csvParser(d, fileName)
	elif extension == 'xml':
		return xmlParser(d, fileName)


def csvParser(d, fileName):
	dList = [] # List of row data dictionaries
	spamReader = []
	file = open(fileName, newline = '')
	# Determine a type of delimiter #
	first_line = file.readline()
	semicolon = match("[a-zA-Z0-9_ ]+;", first_line)
	tab = match("[a-zA-Z0-9_ ]+\t", first_line)
	file.seek(0)

	if tab != None:
		spamReader = csv.reader(file, delimiter = '\t')
	elif semicolon != None:
		spamReader = csv.reader(file, delimiter = ';')

	data = [list(row) for row in spamReader]
	labels = data[0]
	for row in data[1:]:
		dic = d.copy()
		scanRange = min( len(labels), len(row) )
		
		for id in range(0, scanRange):
			label_name = labels[id].lower().strip() # Lowercase all letters to prevent case sensitivity
			elem_data = row[id]
			if label_name in d:
				dic[label_name] = elem_data.strip()
			elif label_name.replace(' ', '_') in d: # Underscores in label names can be replaced with spaces for readability
				dic[label_name.replace(' ', '_')] = elem_data.strip()
		dList.append(dic)

	return(dList)

