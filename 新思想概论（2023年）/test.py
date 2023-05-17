import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(file='判断.json',mode='r',encoding='utf-8') as f:
    a = json.load(fp=f) #去反斜杠
# print(type(a))
# b = a.replace("\\","")

b = a['text']
b = json.loads(b) #去多余引号

print(len(b['BusinessData']['BC_xcqm_tkb_TF']))
# b = json.loads(str(a))

with open(file='a2.json',mode='w',encoding='utf-8') as f:
    json.dump(fp=f,obj=b,ensure_ascii=False,indent=4,separators=(',',':'))
# print(b)
print(type(b))
