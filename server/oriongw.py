"""gateway to Orion / NGSIv2"""

import requests
import json

def get_from_orion(entity_id="", fiware_service="example", fiware_service_path="/example", base_url="http://127.0.0.1:8666", base_path="/orion/v2/entities/"):

	headers = {
		"Fiware-Service": fiware_service,
		"Fiware-ServicePath": fiware_service_path,
		"Accept": "application/json",
		"platform-apikey": "***REMOVED***"
	}

	request_url = f"{base_url}{base_path}{entity_id}"

	#print("Fetching data")
	#print(" --> URL: " + str(request_url))
	response = requests.get(request_url, headers=headers)
	rjson = response.json()
	#print(" --> Response data: " + json.dumps(rjson))

	return rjson

def get_optimasolutions_test():
	rjson = get_from_orion('lamuskakuja-pylvas-slcc-en-t2', 'optimasolutions_t2', '/lamuskakuja/piha_t2', 'http://pan0108.panoulu.net:8000')
	wmodedata = rjson['workingMode']
	wmode = wmodedata['value']
	print(wmode)

if __name__ == '__main__':
	get_optimasolutions_test()
	

"""
curl -X 'GET' -H 'Accept: application/json' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' 'http://pan0108.panoulu.net:8000/orion/v2/entities/lamuskakuja-pylvas-slcc-en-t2'
​
curl -X 'GET' -H 'Accept: application/json' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' 'http://pan0108.panoulu.net:8000/orion/v2/entities/lamuskakuja-pylvas-slg-en-t2'
"""