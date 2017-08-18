#-*- coding:utf-8 -*-
import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def build_uri(endpoint):
	return '/'.join([URL,endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)

def request_method():
	response = requests.get(build_uri('users/wiwj1987ww'))
	print better_print(response.text)

def request_params():
	response = requests.get(build_uri('users'),params={'since':11})
	print btter_print(resonse.text)
	print response.requests.headers
	print response.url

def request_json():
	response = requests.patch(bulid_uri('user'),auth=('wiwj1987ww','wallss1314'),json={'name':'derekwang','email':'294030597@qq.com'})
	print better_print(response.text)
	print response.request.headers
	print response.request.body
	print response.status_code

def requset_json2():
	response = requests.post(build_uri('user/emails'),auth=('wiwj1987ww','wallss1314'),json=['2711532509@qq.com'])
	print better_print(response.text)
	print response.request.headers
	print response.request.body
	print response.status_code

def timeout_request():
	try:
		response = requests.get(build_uri('user/emails'),timeout=10)
		response.raise_for_status()
	except exceptions.Timeout as e:
		print e.message
	except exceptions.HTTPError as e:
		print e.message
	else:
		print response.text
		print response.status_code


def hard_request():
	from requests import Session,Request
	s = Session()
	headers = {'User-Agent':'Mozila1.2.3'}
	req = Request('GET',build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),headers = headers)
	prepped = req.prepare()
	print prepped.body
	print prepped.headers

	resp = s.send(prepped,timeout=5)
	print resp.status_code
	print resp.request.headers
	print resp.text
if __name__ == '__main__':
	hard_request()

