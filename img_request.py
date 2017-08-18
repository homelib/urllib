#-*- coding :utf-8 -*-

import requests

def download_image():
	url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502508231518&di=b5bd3cf4083b1808ed805e32b817b5b2&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F16%2F42%2F96%2F56e58PICAu9_1024.jpg"
	res = requests.get(url,stream=True)
	with open('github_img.jpg','wb') as fd:
		for chunk in res.iter_content(128):
			fd.write(chunk)
	print res.status_code
	print res.reason

download_image()
