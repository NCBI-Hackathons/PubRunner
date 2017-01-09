import argparse
import xml.etree.cElementTree as etree

def processMedlineFile(medlineFile,outFile):
	"""Basic function that iterates through abstracts in a medline file, do a basic word count and save to a file

	Args:
		medlineFile (file): Medline XML file containing abstracts
		outFile (file): File to save output data to
	Returns:
		Nothing

	"""
	abstractCount = 0

	# Iterate through the XML file and stop on each MedlineCitation
	for event, elem in etree.iterparse(medlineFile, events=('start', 'end', 'start-ns', 'end-ns')):
		if (event=='end' and elem.tag=='MedlineCitation'):

			# Let's get the PMID and Abstract elements from the XML
			pmidElements = elem.findall('./PMID')
			abstractElements = elem.findall('./Article/Abstract/AbstractText')

			if len(pmidElements) != 1 or len(abstractElements) != 1:
				continue

			# Pull the values of the PMID and abstract elements
			pmid = pmidElements[0].text
			abstract = abstractElements[0].text

			# Do a very basic word count
			wordCount = len(abstract.split())

			# Prepare and save output to file
			line = "%s\t%d\n" % (pmid,wordCount)
			outFile.write(line)

			abstractCount += 1

	print "%d abstracts processed" % abstractCount

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Little toy example to "process" a Medline abstract file and gives naive word counts for each abstract')
	parser.add_argument('--medlineFile',type=argparse.FileType('r'),required=True,help='Medline file to process')
	parser.add_argument('--outFile',type=argparse.FileType('w'),required=True,help='Output file for word-counts')

	args = parser.parse_args()

	processMedlineFile(args.medlineFile,args.outFile)

