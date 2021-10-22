"""
Wrapper script to execute avrogen

"""

import avrogen
import argparse
from avrogen import write_schema_files
from os.path import join
import os
from sys import argv

import warnings

def main(args):
	warnings.filterwarnings("ignore")
	with open(args.schema, 'r') as schema:
		write_schema_files(schema.read(), args.out)

if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description='CLI tool to generate python classes from Apache Avro Schemas')
	parser.add_argument(
		'--out', 
		metavar='O',
		type=str, 
		default = './schemas/',
		help='output directory')
	parser.add_argument(
		'schema',
		type=str,
		help='avro schema to generate classes for')

	args = parser.parse_args()

	try:
		exit(main(args))
	except Exception as exc:
		print(avrogen.__doc__)
		raise