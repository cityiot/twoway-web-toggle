"""gateway to Orion / NGSIv2"""

import requests
import json

def make_headers(fiware_service, fiware_service_path, accept="application/json"):
	headers = {
		"Fiware-Service": fiware_service,
		"Fiware-ServicePath": fiware_service_path,
		"Accept": accept,
		"platform-apikey": "***REMOVED***"
	}

	return headers

def get_from_orion(entity_id="", fiware_service="example", fiware_service_path="/example", base_url="http://127.0.0.1:8666", base_path="/orion/v2/entities/"):
	headers = make_headers(fiware_service, fiware_service_path)
	request_url = f"{base_url}{base_path}{entity_id}"

	#print("Fetching data")
	#print(" --> URL: " + str(request_url))
	response = requests.get(request_url, headers=headers)
	rjson = response.json()
	#print(" --> Response data: " + json.dumps(rjson))

	return rjson

def get_optimasolutions_test1():
	rjson1 = get_from_orion('riekonmarja-pylvas-slcc-en-t4', 'optimasolutions_t4', '/riekonmarja/pihapylvas_t4', 'http://pan0108.panoulu.net:8000')

	#wmodedata = rjson['workingMode']
	#wmode = wmodedata['value']
	#we actually just pass the json on now
	#print(wmode)
	return rjson1

def get_optimasolutions_test2():
    rjson2 = get_from_orion('riekonmarja-pylvas-slg-en-t4', 'optimasolutions_t4', '/riekonmarja/pihapylvas_t4', 'http://pan0108.panoulu.net:8000')
    return rjson2

def set_optimasolutions_test(idasparams, idasdata):
	headers = make_headers('optimasolutions_t4', '/riekonmarja/pihapylvas_t4')
	#request_url = f"{base_url}{base_path}{entity_id}"
	request_url = f"http://pan0108.panoulu.net:8000/idasdata/iot/d?{idasparams}"

	print(f"Sending set POST: {request_url} : {idasdata}")
	response = requests.post(request_url, data=idasdata)
	#print(dir(response))
	responsetext = response.text
	#print(responsetext) #apparently empty from IDAS
	return responsetext 

def set_optimasolutions_test1(idasdata):
    idasparams = "k=riekonmarja-pylvas-slcc-en-t4-apikey&i=riekonmarja-pylvas-slcc-en-dev-t4"
    return set_optimasolutions_test(idasparams, idasdata)

def set_optimasolutions_test2(idasdata):
    idasparams = "k=riekonmarja-pylvas-slg-en-t4-apikey&i=riekonmarja-pylvas-slg-en-dev-t4"
    return set_optimasolutions_test(idasparams, idasdata)

if __name__ == '__main__':
	print(get_optimasolutions_test1())
	#print(set_optimasolutions_test('wms|automatic'))

	#print(set_optimasolutions_test('wms|manual'))
	#print(set_optimasolutions_test('pss|on'))
	#print(set_optimasolutions_test('pss|off'))


"""
curl -X 'GET' -H 'Accept: application/json' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' 'http://pan0108.panoulu.net:8000/orion/v2/entities/lamuskakuja-pylvas-slcc-en-t2'
​
curl -X 'GET' -H 'Accept: application/json' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' 'http://pan0108.panoulu.net:8000/orion/v2/entities/lamuskakuja-pylvas-slg-en-t2'
"""

"""
# Ohjaus tapahtuu seuraavalla tavalla:

# workingModeSet ==> tilaan automatic
curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'wms|automatic' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slcc-en-t2-apikey&i=lamuskakuja-pylvas-slcc-en-dev-t2'

# workingModeSet ==> tilaan manual

curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'wms|manual' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slcc-en-t2-apikey&i=lamuskakuja-pylvas-slcc-en-dev-t2'

# powerStateSet ==> tilaan on

curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'pss|on' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slg-en-t2-apikey&i=lamuskakuja-pylvas-slg-en-dev-t2'

# powerStateSet ==> tilaan off

curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'pss|off' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slg-en-t2-apikey&i=lamuskakuja-pylvas-slg-en-dev-t2'
"""

#---

"""
# Ohjaus tapahtuu seuraavalla tavalla:

# workingModeSet ==> tilaan automatic
curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'wms|automatic' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slcc-en-t2-apikey&i=lamuskakuja-pylvas-slcc-en-dev-t2'

# workingModeSet ==> tilaan manual

curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'wms|manual' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slcc-en-t2-apikey&i=lamuskakuja-pylvas-slcc-en-dev-t2'

# powerStateSet ==> tilaan on

curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'pss|on' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slg-en-t2-apikey&i=lamuskakuja-pylvas-slg-en-dev-t2'

# powerStateSet ==> tilaan off

curl -X 'POST' -H 'Content-Type: text/plain' -H 'Fiware-Service: optimasolutions_t2' -H 'Fiware-ServicePath: /lamuskakuja/piha_t2' \
-d 'pss|off' \
'{http://pan0108.panoulu.net}:8000/idasdata/iot/d?k=lamuskakuja-pylvas-slg-en-t2-apikey&i=lamuskakuja-pylvas-slg-en-dev-t2'

"""