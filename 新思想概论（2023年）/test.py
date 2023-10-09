import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(file='test.json',mode='r',encoding='utf-8') as f:
    a = json.load(fp=f) #去反斜杠
# print(type(a))
# b = a.replace("\\","")

b = a['text']
b = json.loads(b) #去多余引号
a['text'] = b
# print(len(b['BusinessData']['BC_xcqm_tkb_TF']))
# b = json.loads(str(a))

with open(file='test2.json',mode='w',encoding='utf-8') as f:
    json.dump(fp=f,obj=a,ensure_ascii=False,indent=4,separators=(',',':'))
# print(b)
print(type(b))
