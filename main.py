import requests
import json
import time

start = time.time()

url = 'http://romateks.pakabulut.com:6767/'
connect = 'integratorservice/connect'
r = requests.get(url=url + connect)
print(r.status_code)
session_id = json.loads(r.content)['SessionID']
order_url = '(S(%s))/integratorservice/RunProc?{"ProcName": "sp_MT_StoreSales","Parameters": [{"Name": "StartDate",' \
            '"Value": "20230101"},{"Name": "EndDate","Value": "20230102"}]}' % session_id
r1 = requests.get(url=url + order_url)
print(r1.status_code)
end = time.time()
print(round(end - start))
