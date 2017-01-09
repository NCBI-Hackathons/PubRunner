import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Little toy example to "process" a Medline abstract file and gives naive word counts for each abstract')
	parser.add_argument('-i',required=True,help='Medline folder to process')
	parser.add_argument('-o',required=True,help='Output folder for word-counts')
	
	args = parser.parse_args()

	raise RuntimeError('This fails every time')
