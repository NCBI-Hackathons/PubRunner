from settings import *
import os
from subprocess import run, PIPE
import datetime
import resource
import shutil
import sys
import traceback
from FTPClient import *
import requests
import json

class Runner:
	def __init__(self, params):
		# Load everything from the object translated from the JSON file
		self.__dict__ = params

	def run(self):
		self.success = False
		tries = 0
		while not self.success and tries < FAIL_LIMIT:
			# Make sure that the directory for output is created
			destination = ROOT+OUTPUT+self.name+"/"+self.version+"/"
			if not os.path.isdir(destination+"PubRunnerLogs/"):
				os.makedirs(destination+"PubRunnerLogs/")

			try:


				# Set log files
				stderrf = open(destination+"PubRunnerLogs/std.err","wb")
				stdoutf = open(destination+"PubRunnerLogs/std.out","wb")
				process = run([self.command,
							  "tools/"+self.name+"/"+self.version+"/"+self.main,
							  "-i",ROOT+DB,
							  "-o",destination],
							  stdout=stdoutf,
							  stderr=stderrf,
							  timeout=self.timeout,
							  check=True)

				self.success = True
			except:
				#print (Exception, err)
				#traceback.print_exc()
				tries += 1
				pass
			self.lastRun = datetime.datetime.now().strftime("%m-%d-%Y")

			# Also log PubRunner data information
			with open(destination+"PubRunnerLogs/info.txt", "w") as f:
				f.write("PubRunner version: "+str(VERSION)+"\nRun on "+self.lastRun)

	def pushToFTP(self):
		assert FTP_ADDRESS != '', 'FTP address must be completed in the setting.py file'
		assert FTP_USERNAME != '', 'FTP username must be completed in the setting.py file'
		assert FTP_PASSWORD != '', 'FTP password must be completed in the setting.py file'

		output = ROOT+OUTPUT+self.name+"/"+self.version+"/"

		# N.B. This doesn't recursively copy files

		# Push output folder contents
		# 1. Set up FTP
		ftpc = FTPClient(FTP_ADDRESS, FTP_USERNAME, FTP_PASSWORD)
		# 2. Go the the right directory, or create it
		ftpc.cdTree(self.name+"/"+self.version+"/")
		# 3. Upload all files
		for f in os.listdir(output):
			fPath = os.path.join(output, f)
			if os.path.isfile(fPath):
				ftpc.upload(output, f)
		# 4. Close session
		ftpc.quit()

		# Delete that content locally
		for f in os.listdir(output):
			fPath = os.path.join(output, f)
			try:
				if os.path.isfile(fPath):
					os.unlink(fPath)
			except Exception as e:
				print(e)
	
	def pushToLocalDirectory(self):
		assert LOCAL_DIRECTORY != '', 'Local directory must be completed in the setting.py file'

		output = ROOT+OUTPUT+self.name+"/"+self.version+"/"

		destDir = LOCAL_DIRECTORY.rstrip("/")+"/"+self.name+"/"+self.version+"/"
		if not os.path.isdir(destDir):
			os.makedirs(destDir)

		# N.B. This doesn't recursively copy files
		for f in os.listdir(output):
			src = os.path.join(output, f)
			dst = os.path.join(destDir, f)
			if os.path.isfile(src):
				shutil.copyfile(src,dst)

		# Delete that content locally
		for f in os.listdir(output):
			fPath = os.path.join(output, f)
			try:
				if os.path.isfile(fPath):
					os.unlink(fPath)
			except Exception as e:
				print(e)

	def pushToZenodo(self):
		ZENODO_URL = 'https://sandbox.zenodo.org'

		with open('.zenodo_token','r') as f:
			ACCESS_TOKEN = f.read().strip()
		
		output = ROOT+OUTPUT+self.name+"/"+self.version+"/"

		print("  Creating new Zenodo submission")
		headers = {"Content-Type": "application/json"}
		r = requests.post(ZENODO_URL + '/api/deposit/depositions',
						params={'access_token': ACCESS_TOKEN}, json={},
						headers=headers)

		assert r.status_code == 201, "Unable to create Zenodo submission (error: %d) " % r.status_code

		bucket_url = r.json()['links']['bucket']
		deposition_id = r.json()['id']
		doi = r.json()["metadata"]["prereserve_doi"]["doi"]
		doiURL = "https://doi.org/" + doi
		print("  Got provisional DOI: %s" % doiURL)

		print("  Adding files to Zenodo submission")
		for f in os.listdir(output):
			src = os.path.join(output, f)
			if os.path.isfile(src):
				r = requests.put('%s/%s' % (bucket_url,f),
								data=open(src, 'rb'),
								headers={"Accept":"application/json",
								"Authorization":"Bearer %s" % ACCESS_TOKEN,
								"Content-Type":"application/octet-stream"})


				assert r.status_code == 200, "Unable to add file to Zenodo submission (error: %d) " % r.status_code

		print("  Adding metadata to Zenodo submission")
		data = {
				'metadata': {
						'title': self.name,
						'upload_type': 'dataset',
						'description':	'Results from tool executed using PubRunner on MEDLINE corpus',
						'creators': [{'name': ZENODO_AUTHOR,
								'affiliation': ZENODO_AUTHOR_AFFILIATION}]
				}
		}

		requests.put(ZENODO_URL + '/api/deposit/depositions/%s' % deposition_id,
						params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
						headers=headers)

		assert r.status_code == 200, "Unable to metadata to Zenodo submission (error: %d) " % r.status_code

		print("  Publishing Zenodo submission")
		r = requests.post(ZENODO_URL + '/api/deposit/depositions/%s/actions/publish' % deposition_id,
						 params={'access_token': ACCESS_TOKEN} )
		assert r.status_code == 202, "Unable to publish to Zenodo submission (error: %d) " % r.status_code

		return doiURL

