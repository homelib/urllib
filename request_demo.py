#_*_ coding: utf_8 _*_

import requests

URL_IP = 'http://127.0.0.1:8000/ip'

def use_simple_requests():
	response = requests.get(URL_IP)
	print '>>>>Respnese Headers:'
	print response.headers
	print '>>>>Response Body:'
	print response.text

def use_params_requests():
	params = {'params1':'hello','params2':'world'}
	response  = requests.get(URL_IP,params=params)
	print '>>>>Respnese Headers:'
	print response.headers
	print '>>>>Status Code'
	print response.status_code
	print '>>>>Response Body:'
	print response.json()

if __name__ =='__main__':
	print '>>>Use simple requests'
	use_simple_requests()
	print '>>>Use params requests'
	use_params_requests()
