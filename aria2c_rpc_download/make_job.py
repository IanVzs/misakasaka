import sys
sys.path.append("..")
import config
import json
import requests

url = sys.argv[1]
jsonreq = json.dumps({'jsonrpc':'2.0', 'id':'qwer','method':'aria2.addUri','params':[[url]]}) 
aaa = requests.post(config.URL_SERVER_ARIA2, jsonreq)
print(aaa.json())
