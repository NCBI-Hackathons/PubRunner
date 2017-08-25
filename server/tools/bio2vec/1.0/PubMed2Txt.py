import argparse
import xml.etree.cElementTree as etree
import os
from os import listdir
from os.path import isfile, join
import codecs
import re
from six.moves import html_parser

# Remove empty brackets (that could happen if the contents have been removed already
# e.g. for citation ( [3] [4] ) -> ( ) -> nothing
def removeBracketsWithoutWords(text):
	fixed = re.sub(r'\([\W\s]*\)', ' ', text)
	fixed = re.sub(r'\[[\W\s]*\]', ' ', fixed)
	fixed = re.sub(r'\{[\W\s]*\}', ' ', fixed)
	return fixed

# Some older articles have titles like "[A study of ...]."
# This removes the brackets while retaining the full stop
def removeWeirdBracketsFromOldTitles(titleText):
	titleText = titleText.strip()
	if titleText[0] == '[' and titleText[-2:] == '].':
		titleText = titleText[1:-2] + '.'
	return titleText

# Unescape HTML special characters e.g. &gt; is changed to >
htmlParser = html_parser.HTMLParser()
def htmlUnescape(text):
	return htmlParser.unescape(text)

# XML elements to ignore the contents of
ignoreList = ['table', 'table-wrap', 'xref', 'disp-formula', 'inline-formula', 'ref-list', 'bio', 'ack', 'graphic', 'media', 'tex-math', 'mml:math', 'object-id', 'ext-link']

# XML elements to separate text between
separationList = ['title', 'p', 'sec', 'break', 'def-item', 'list-item', 'caption']
def extractTextFromElem(elem):
	textList = []
	
	# Extract any raw text directly in XML element or just after
	head = ""
	if elem.text:
		head = elem.text
	tail = ""
	if elem.tail:
		tail = elem.tail
	
	# Then get the text from all child XML nodes recursively
	childText = []
	for child in elem:
		childText = childText + extractTextFromElem(child)
		
	# Check if the tag should be ignore (so don't use main contents)
	if elem.tag in ignoreList:
		return [tail.strip()]
	# Add a zero delimiter if it should be separated
	elif elem.tag in separationList:
		return [0] + [head] + childText + [tail]
	# Or just use the whole text
	else:
		return [head] + childText + [tail]
	

# Merge a list of extracted text blocks and deal with the zero delimiter
def extractTextFromElemList_merge(list):
	textList = []
	current = ""
	# Basically merge a list of text, except separate into a new list
	# whenever a zero appears
	for t in list:
		if t == 0: # Zero delimiter so split
			if len(current) > 0:
				textList.append(current)
				current = ""
		else: # Just keep adding
			current = current + " " + t
			current = current.strip()
	if len(current) > 0:
		textList.append(current)
	return textList
	
# Main function that extracts text from XML element or list of XML elements
def extractTextFromElemList(elemList):
	textList = []
	# Extracts text and adds delimiters (so text is accidentally merged later)
	if isinstance(elemList, list):
		for e in elemList:
			textList = textList + extractTextFromElem(e) + [0]
	else:
		textList = extractTextFromElem(elemList) + [0]

	# Merge text blocks with awareness of zero delimiters
	mergedList = extractTextFromElemList_merge(textList)
	
	# Remove any newlines (as they can be trusted to be syntactically important)
	mergedList = [ text.replace('\n', ' ') for text in mergedList ]
	
	return mergedList

def processMedlineFolder(medlineFolder,outFolder):
	"""
	Basic function that iterates through abstracts in a medline file and extracts the title and abstract text.

	Args:
		medlineFolder (folder): Medline XML folder containing abstracts
		outFolder (folder): Folder to save output data to
	Returns:
		Nothing

	"""
	abstractCount = 0

	# List of all files in the directory
	files = [ f for f in listdir(medlineFolder) if isfile(join(medlineFolder, f)) ]
	
	# Filter for only XML files
	files = [ f for f in files if f.endswith('xml') ]

	# Sort the files so it's easier to see
	files = sorted(files)

	# Iterate over all files
	for i,f in enumerate(files):
		print("Processing %s (%d/%d)" % (f,(i+1),len(files)))
		fullInPath = os.path.join(medlineFolder,f)
		fullOutPath = os.path.join(outFolder,f.replace('.xml','.txt'))

		with codecs.open(fullOutPath,'w','utf-8') as outF:
			# Iterate through the XML file and stop on each MedlineCitation
			for event, elem in etree.iterparse(fullInPath, events=('start', 'end', 'start-ns', 'end-ns')):
				if (event=='end' and elem.tag=='MedlineCitation'):
			
					# Extract the title of paper
					title = elem.findall('./Article/ArticleTitle')
					titleText = extractTextFromElemList(title)
					titleText = [ removeWeirdBracketsFromOldTitles(t) for t in titleText ]
					
					# Extract the abstract from the paper
					abstract = elem.findall('./Article/Abstract/AbstractText')
					abstractText = extractTextFromElemList(abstract)
				
					allText = titleText + abstractText
					allText = [ t for t in allText if len(t) > 0 ]
					allText = [ t for t in allText if len(t) > 0 ]
					allText = [ htmlUnescape(t) for t in allText ]
					allText = [ removeBracketsWithoutWords(t) for t in allText ]

					# Add lots of new lines after each entry
					allText = [ "%s\n\n" % t for t in allText ]

					outF.write("".join(allText))
					abstractCount += 1

					# Important: clear the current element from memory to keep memory usage low
					elem.clear()

	print("%d abstracts processed" % abstractCount)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Script that takes in a set of Pubmed XML files, extracts the title and abstracts and converts them to TXT files')
	parser.add_argument('-i',required=True,help='Input folder with XML files')
	parser.add_argument('-o',required=True,help='Output folder with TXT UTF-8 files')

	args = parser.parse_args()

	processMedlineFolder(args.i,args.o)
