import sys
import requests
import json

with open('.accesstoken','r') as f:
	ACCESS_TOKEN = f.read().strip()

r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
			params={'access_token': ACCESS_TOKEN}, json={},
			headers={"Content-Type": "application/json"})

print r.status_code

bucket_url = r.json()['links']['bucket']

filename='bigfile.txt'
r = requests.put('%s/%s' % (bucket_url,filename),
		data=open(filename, 'rb'),
		headers={"Accept":"application/json",
		"Authorization":"Bearer %s" % ACCESS_TOKEN,
		"Content-Type":"application/octet-stream"})

print r.status_code

