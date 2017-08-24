import sys
import requests
import json

if __name__ == '__main__':
	with open('.accesstoken','r') as f:
		ACCESS_TOKEN = f.read().strip()

	#r = requests.get('https://sandbox.zenodo.org/api/deposit/depositions',
	#		params={'access_token': ACCESS_TOKEN})

	headers = {"Content-Type": "application/json"}
	r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
				params={'access_token': ACCESS_TOKEN}, json={},
				headers=headers)

	print r.status_code
	print json.dumps(r.json(),indent=2,sort_keys=True)

	deposition_id = r.json()['id']
	data = {'filename': 'myfirstfile.txt'}
	files = {'file': open('myfirstfile.txt', 'rb')}
	r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
			params={'access_token': ACCESS_TOKEN}, data=data,
			files=files)

	print r.status_code
	print json.dumps(r.json(),indent=2,sort_keys=True)

	data = {
		'metadata': {
			'title': 'My first upload',
			'upload_type': 'dataset',
			'description': 'This is my first upload',
			'creators': [{'name': 'Doe, John',
				'affiliation': 'Zenodo'}]
		}
	}

	requests.put('https://sandbox.zenodo.org/api/deposit/depositions/%s' % deposition_id,
			params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
			headers=headers)

	print r.status_code
	print json.dumps(r.json(),indent=2,sort_keys=True)

	#r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/%s/actions/publish' % deposition_id,
	#		params={'access_token': ACCESS_TOKEN} )
	#print r.status_code
