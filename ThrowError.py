import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Little toy example to "process" a Medline abstract file, but really to just fail')
	parser.add_argument('--medlineFile',type=argparse.FileType('r'),required=True,help='Medline file to process')
	parser.add_argument('--outFile',type=argparse.FileType('w'),required=True,help='Output file (that will not be filled)')

	args = parser.parse_args()

	raise RuntimeError('This fails every time')

