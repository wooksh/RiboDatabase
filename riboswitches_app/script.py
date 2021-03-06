'''
# First argument is filename for csv parser
	python3 script.py switche2.csv
# To delete all data in all tables without removing tables themselves using manage.py:
	python3 manage.py flush --noinput
# To delete single model data:
	ModelName.objects.all().delete()
# To import only a few models:
	from database.models import RiboFamily, RiboClass

USAGE:
python3 script.py loadresults		- to load all annotation results
python3 script.py loadresults purge 	- to load all annotation results and before that purge whole database

'''

from parser import loadDataToDictionary
import os
from sys import argv, exit
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from re import match
from datetime import datetime, timedelta
from time import sleep, localtime, strftime

''' This tells Django where to look for our project's settings '''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riboswitches_app.settings")
''' This allows to load our models' file '''
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
''' Finally import out models '''
from database.models import *
''' To use managing functions inside script: '''
from django.core.management import execute_from_command_line

### HANDLE SCRIPT PARAMETERS ###
result_files = []
isResult = False

if len(argv) == 1:
	print("No arguments where passed to the script. Program will abort now...")
elif argv[1] == "loadresults":
	result_files = [ file for file in os.listdir('../Riboswitches/Results') ]
	isResult = True
else:
	result_files = [ argv[1] ]

if len(argv) >= 3 and argv[2] == "purge":
	execute_from_command_line([argv[0], 'flush', '--noinput'])



def imageValidation(name):
	rasterFormats = ['jpeg', 'jpg', 'jfif', 'gif', 'bmp', 'png', 'tiff']
	temp = name.split('.')
	extension = name.split('.')[1] if len(temp) == 2 else ""
	
	if extension in rasterFormats:
		return(True)
	else:
		return(False)

def convertToList(line, delimiter = ','):
	if line != '' and line != None:
		line = line.split(delimiter)
		return([elem.strip() for elem in line])
	else:
		return([])


def convertToListForInt(line, delimiter = ','):
	if not isinstance(line, int):
		if line != '':
			line = line.split(delimiter)
			return([int(elem.strip()) for elem in line])
		else:
			return([])
	else:
		return([line])

def convertToListForFloat(line, delimiter = ','): # Modified for floats
	if not isinstance(line, float):
		if line != '':
			line = line.split(delimiter)
			return([float(elem.strip()) for elem in line])
		else:
			return([])
	else:
		return([line])

def minimumButNotZero(*args):
	if len(args) > 0:
		li = [l for l in args if l > 0]
		if li != []:
			return( min(li) ) 
		else: 
			return(0)
	else:
		return(0)

def maximum(*args):
	if len(args) > 0:
		return( max(l for l in args) )
	else:
		return(0)

def indexOutOfRange(_list, id):
	isIt = False if id < len(_list) else True
	return(isIt)


##### SCRIPT STARTS HERE #####
record_counter = 0
a = datetime.now()

for datafile in result_files:
	if isResult:
		dList = loadDataToDictionary(datafile, True)
	else:
		dList = loadDataToDictionary(datafile, False)

	record_counter += len(dList)

	for row in dList:
		''' CREATING NEW OBJECTS '''
		v_record = None
		v_riboclass = None
		v_ribofamily = None
		v_organism = None
		v_gene = None
		v_taxonomy = None
		v_mech_conf = None

		''' ARRAYS '''
		v_articles = []
		v_operon_genes = []
		v_structures3d = []
		v_ligands = []
		v_ligandclasses = []
		v_taxonomies = []
		# Aptamers #
		v_aptamers = []
		v_structures2d = []


		''' LigandClass '''
		v_ligandclass_name = convertToList(row['ligand_class_name'])
		v_ligandclass_desc = convertToList(row['ligand_class_description'])

		lc_count = len(v_ligandclass_name)

		for id in range(0, lc_count):
			try:
				if v_ligandclass_name[id] != '':
					temp_ligandclass = LigandClass.objects.create(
						name = v_ligandclass_name[id],
						)
					if not indexOutOfRange(v_ligandclass_desc, id):
						temp_ligandclass.description = v_ligandclass_desc[id]
						temp_ligandclass.save()
					v_ligandclasses.append(temp_ligandclass)
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					temp_ligandclass = LigandClass.objects.get(name = v_ligandclass_name[id])
					v_ligandclasses.append(temp_ligandclass)


		''' Ligand - ManyToMany'''
		v_ligand_name = convertToList(row['ligand_name'])
		v_ligand_desc = convertToList(row['ligand_description'])
		v_ligand_img = convertToList(row['image_name'])

		ligand_count = len(v_ligand_name)

		for id in range(0, ligand_count):
			try:
				if v_ligand_name[id] != '':
					temp_ligand = Ligand.objects.create(
						name = v_ligand_name[id],
						)
					if not indexOutOfRange(v_ligandclasses, id):
						temp_ligand.ligand_class = v_ligandclasses[id]
					if not indexOutOfRange(v_ligand_desc, id):
						temp_ligand.description = v_ligand_desc[id]
					if not indexOutOfRange(v_ligand_img, id) and imageValidation(v_ligand_img[id]):
						temp_ligand.image_name = v_ligand_img[id]

					temp_ligand.save()
					v_ligands.append(temp_ligand)
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					temp_ligand = Ligand.objects.get(name = v_ligand_name[id])
					v_ligands.append(temp_ligand)


		''' RiboClass '''
		try:
			if row['class_name'] != '':
				v_riboclass = RiboClass.objects.create(
					name = row['class_name'], # Primary Key
					description = row['class_description'],
					alignment = row['class_alignment'],
				)
		except IntegrityError as e:
			if match("UNIQUE", str(e)):
				v_riboclass = RiboClass.objects.get(name = row['class_name'])


		''' RiboFamily '''
		
		if row['family_name'] != '':
			try:
				v_ribofamily = RiboFamily.objects.create(
					ribo_class = v_riboclass,
					name = row['family_name'], # Primary Key
					description = row['family_description'],
					alignment = row['family_alignment'],
				)
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					v_ribofamily = RiboFamily.objects.get(name = row['family_name'])

		elif row['family_name'] == '' and row['class_name'] != '':
			try:
				v_ribofamily = RiboFamily.objects.create(
					ribo_class = v_riboclass,
					name = row['class_name'], # Primary Key
					description = '',
					alignment = '',
				)
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					v_ribofamily = RiboFamily.objects.get(name = row['class_name'])


		''' Structure 3D '''
		pdb_ids = convertToList(row['structure_3d'])

		for pdb in pdb_ids:
			try:
				if pdb != '':
					Structure3D.objects.create(
						pdbid = pdb,
						ribo_class = v_riboclass,
					)
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					print('Error. Object Structure3D has been already assigned to RiboClass. {}'.format(str(e)) )
				else:
					print(e)


		''' Taxonomy '''
		tax_names = convertToList(row['taxonomy_name'])

		if not isinstance(row['taxonomy_id'], int):
			tax_ids = convertToListForInt(row['taxonomy_id'])
		elif isinstance(row['taxonomy_id'], int): # Because default value is Integer 0
			tax_ids = []

		if tax_names != []:
			complete_coordinates = minimumButNotZero( len(tax_ids), len(tax_names) )

			tax_ids = tax_ids[::-1]
			tax_names = tax_names[::-1]

			for id in range(0, complete_coordinates):
				v_taxonomy = None
				try:
					if not id > 0:
						v_taxonomy = Taxonomy.objects.create(
							taxonomy_id = tax_ids[id],
							name = tax_names[id],
						)
					else:
						v_taxonomy = Taxonomy.objects.create(
							taxonomy_id = tax_ids[id],
							name = tax_names[id],
							parent = v_taxonomies[id - 1]
						)
				except IntegrityError as e:
					if match("UNIQUE", str(e)):
						v_taxonomy = Taxonomy.objects.get(taxonomy_id = tax_ids[id])

				v_taxonomies.append(v_taxonomy)
		elif tax_ids != [] and tax_names == []:
			for id in tax_ids:
				if not Taxonomy.objects.filter(taxonomy_id = id):
					os.system("python3 ../riboswitches_app/tax_parser.py {}".format(id))
					os.system("python3 ../riboswitches_app/script.py ../riboswitches_app/taxonomy.csv")
					os.system("rm ../riboswitches_app/taxonomy.csv")


		''' Organism '''
		try:
			if row['build_id'] != '':
				if tax_ids != []:
					v_organism = Organism.objects.create(
 
						scientific_name = Taxonomy.objects.get(taxonomy_id = tax_ids[0]).name, 
						common_name = row['common_name'],
						accession_number = row['organism_accession_number'],
						build_id = row['build_id'],
						taxonomy = Taxonomy.objects.get(taxonomy_id = tax_ids[0]),
					)
				else:
					v_organism = Organism.objects.create(
						scientific_name = row['scientific_name'],
						common_name = row['common_name'],
						accession_number = row['organism_accession_number'],
						build_id = row['build_id'],
					)

		except IntegrityError as e:
			if match("UNIQUE", str(e)):
				v_organism = Organism.objects.get(build_id = row['build_id'])
				if v_taxonomies != []: # If an organism already exists and taxonomy was given, assign the taxonomy to the organism
					v_organism.taxonomy = v_taxonomies[-1]
					v_organism.save()


		''' Gene '''
		try:
			if row['gene_name'] != '':
				v_gene = Gene.objects.create(
					organism = v_organism, 
					name = row['gene_name'],
					locus_tag = row['locus_tag'],
				)

				if row['gene_start'] != 0 or row['gene_end'] != 0:
					v_gene.position = Position.objects.create(
						start = row['gene_start'],
						end = row['gene_end'],
						strand = row['strand'],
						location = row['location'],
					)
				else:
					v_gene.position = None
				v_gene.save()
		except IntegrityError as e:
			if match("UNIQUE", str(e)):
				v_gene = Gene.objects.get(organism = v_organism, name = row['gene_name'])
		

		''' Structure2D '''
		v_predicted = convertToList(row['predicted'])
		v_with_ligand = convertToList(row['with_ligand'])
		v_without_ligand = convertToList(row['without_ligand'])

		biggest_length = maximum(len(v_predicted), len(v_with_ligand), len(v_without_ligand))

		for id in range(0, biggest_length):
			temp_struc = Structure2D.objects.create(
				without_ligand = Structure2D._meta.get_field('without_ligand').get_default() if indexOutOfRange(v_without_ligand, id) else v_without_ligand[id],
				with_ligand = Structure2D._meta.get_field('with_ligand').get_default() if indexOutOfRange(v_with_ligand, id) else v_with_ligand[id],
				predicted = Structure2D._meta.get_field('predicted').get_default() if indexOutOfRange(v_predicted, id) else v_predicted[id],
			)
			v_structures2d.append(temp_struc)


		''' Article - ManyToMany relation '''
		article_ids = convertToList(row['articles'])
		temp_art = None

		for art in article_ids:
			try:
				if art != '': # NOT NULL exception is not threw in IntegerField, so I prevented adding wrong data this way
					temp_art = Article.objects.create(pmid = art)
					v_articles.append(temp_art)
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					temp_art = Article.objects.get(pmid = art)
					v_articles.append(temp_art)


		''' Operon Genes - ManyToMany relation ogarnac wczytywanie wielu genow w encji gen'''
		operon_list = convertToList(row['operon_genes'])
		temp_gene = None

		for gene in operon_list:
			try:
				temp_gene = Gene.objects.get(organism = v_organism, name = gene)
			except ObjectDoesNotExist: 
				temp_gene = Gene.objects.create(
					organism = v_organism, 
					name = gene,
					position = None,
				)
			v_operon_genes.append(temp_gene)


		''' Mechanism '''
		_mechanism = 'UN'
		if row['mechanism'] == 'translation':
			_mechanism = 'TRL'
		elif row['mechanism'] == 'transcription':
			_mechanism = 'TRN'
		elif row['mechanism'] == 'degradation':
			_mechanism = 'DG'


		''' Switch '''
		if v_gene != None:
			v_record = Record.objects.create(
				family = v_ribofamily,
				gene = v_gene,
				effect = row['effect'],
				mechanism = _mechanism,
				sequence = row['sequence'],
			)
		else:
			continue


		''' Mechanism Confirmation '''
		if row['confirmation'] != '' and row['confirmation'] != None:
			try:
				v_mech_conf = Article.objects.create(pmid = row['confirmation'])
			except IntegrityError as e:
				if match("UNIQUE", str(e)):
					v_mech_conf = Article.objects.get(pmid = row['confirmation'])
			v_mech_conf.save()
			v_record.mechanism_confirmation = v_mech_conf
		else:
			v_record.mechanism_confirmation = None


		''' Terminator '''
		if row['terminator_start'] != 0 or row['terminator_end'] != 0:
			v_record.terminator = Position.objects.create(
				start = row['terminator_start'], 
				end = row['terminator_end'],
				location = row['location'],
				strand = row['strand'],
				score = row['terminator_score'],
				)
		else:
			v_record.terminator = None
			

		''' Promotor '''
		if row['promoter_start'] != 0 or row['promoter_end'] != 0:
			v_record.promoter = Position.objects.create(
				start = row['promoter_start'], 
				end = row['promoter_end'],
				location = row['location'],
				strand = row['strand'],
				score = row['promoter_score'],
				)
		else:
			v_record.promoter = None


		''' Shine-Dalgarno '''
		if row['sd_start'] != 0 or row['sd_end'] != 0:
			v_record.shinedalgarno = Position.objects.create(
				start = row['sd_start'], 
				end = row['sd_end'],
				location = row['location'],
				strand = row['strand'],
				score = row['sd_score'],
				)
		else:
			v_record.shinedalgarno = None


		v_record.save()


		''' Aptamer '''
		v_ap_start = convertToListForInt(row['aptamer_start'])
		v_ap_end = convertToListForInt(row['aptamer_end'])
		v_ap_score = convertToListForFloat(row['aptamer_score'])
		v_ap_temp = None
		#v_structures2d

		complete_coordinates = minimumButNotZero( len(v_ap_start), len(v_ap_end) ) # It's a number of complete pairs of values [start, end]
		biggest_length = complete_coordinates

		if not(len(v_ap_start) <= 1 and len(v_ap_end) <= 1 and v_ap_start[0] == 0 and v_ap_end[0] == 0):
			for id in range(0, biggest_length):
				v_ap_temp = Aptamer.objects.create(switch = v_record)

				v_ap_temp.position = Position.objects.create(
					start = Position._meta.get_field('start').get_default() if indexOutOfRange(v_ap_start, id) else v_ap_start[id], 
					end = Position._meta.get_field('end').get_default() if indexOutOfRange(v_ap_end, id) else v_ap_end[id],
					location = row['location'],
					strand = row['strand'],
				)

				if not indexOutOfRange(v_structures2d, id):
					v_ap_temp.structure = v_structures2d[id]

				if not indexOutOfRange(v_ap_score, id):
					v_ap_temp.position.score = v_ap_score[id]
					v_ap_temp.position.save()

				v_ap_temp.save()


		''' Add ManyToMany relations '''
		# Articles #
		for it in v_articles:
			v_record.articles.add(it)
		v_record.save()
		# Operon genes #
		for it in v_operon_genes:
			v_record.genes_under_operon_regulation.add(it)
		v_record.save()
		# Ligands #
		for it in v_ligands:
			v_riboclass.ligands.add(it) # Zmienić na klasę


print('Done loading {} records, date: {}'.format(record_counter, str(strftime("%a, %d %b %Y %H:%M:%S", localtime()))))
b = datetime.now()
c = b - a
#print("{} seconds {} microseconds\n---".format(c.seconds, c.microseconds % c.seconds))
