#coding:utf8
import requests
import json

#录音
from record import Record

record = Record(channels=1)
audioData = record.record(2)

#获取token
from secret import API_KEY,SECRET_KEY
authUrl = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id="+API
+"&client_secret="+SECRET_KEY;

response = requests.get(authUrl)
res = json.loads(response.content)
token = res['access_token']

#语音识别
cuid = 'xxxxxxxxx'
srvUrl = 'http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token
httpHeader = {
	'Content-Type':'audio/wav; rate = 8000',

}
response = requests.post(srvUrl,headers=httpHeader,data=audioData)
res = json.loads(response.content)
text = res['result'][0]

print u'\n识别结果:'
print text