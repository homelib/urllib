#-*- coding : utf-8 -*-

import requests

BASE_URL = 'https://api.github.com'

def current_url(end_point):
	return '/'.join([BASE_URL,end_point])

def basic_auth():
	response = requests.get(current_url('user'),auth=('immocdemo','immocdemo123'))
	print response.text
	print response.request.headers

basic_auth() 
