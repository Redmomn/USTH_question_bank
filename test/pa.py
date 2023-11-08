import json,os,requests,time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

kcbm = 1000
headers = {'Content-Type': 'application/json'}

for i in range(1000,2000):
    body = {
        "BPOName": "BPO_32342",
        "MethodName": "BusiViewStringJson",
        "Parameters": {
            "urlParams": 1
        },
        "PUrl": {
            "kcbm": f"{i}"
        },
        "ClassFullName": "",
        "GloalServiceName": "",
        "openid": "",
        "fRegisterBPO": "true"
    }

    res = requests.post('http://140.143.140.141/api/ServiceEntryForJson.ashx',data=json.dumps(body),headers=headers)

    with open(f'{i}.json',mode='w',encoding='utf-8') as fp:
        fp.write(res.text)
    
    print(f'{i} is OK')
    
    time.sleep(1.5)
