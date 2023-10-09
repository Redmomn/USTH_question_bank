import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def ayns(filename):
    with open(file=filename,mode='r',encoding='utf-8') as f:
        a = json.load(fp=f) #去反斜杠
# print(type(a))
# b = a.replace("\\","")

    b = a['text']
    b = json.loads(b) #去多余引号
    # print(b)
    b:dict = b["BusinessData"]
    if "BC_xcqm_tkb_SC" in b.keys():
        return b["BC_xcqm_tkb_SC"]
    elif "BC_xcqm_tkb_MC" in b.keys():
        return b["BC_xcqm_tkb_MC"]
    elif "BC_xcqm_tkb_TF" in b.keys():
        return b["BC_xcqm_tkb_TF"]
    elif "BC_xsgm_xssjb_x_sc" in b.keys():
        return b["BC_xsgm_xssjb_x_sc"]
    elif "BC_xsgm_xssjb_x_mc" in b.keys():
        return b["BC_xsgm_xssjb_x_mc"]
    elif "BC_xsgm_xssjb_x_tf" in b.keys():
        return b["BC_xsgm_xssjb_x_tf"]

sct = ayns('..\\新思想概论（2023年）\\单选.json')
mct = ayns('..\\新思想概论（2023年）\\多选.json')
tft = ayns('..\\新思想概论（2023年）\\判断.json')
dxt = ayns('test.json')

if dxt[0]['stlx'] == 'SC':
    te = sct
elif dxt[0]['stlx'] == 'MC':
    te = mct
elif dxt[0]['stlx'] == 'TF':
    te = tft
da_l = {}
for i in dxt:
    for w in te:
        if i['wt'] == w['wt']:
            xx = str(i['txxh'])
            da_l[xx] = w['da']
            break


# print(len(b['BusinessData']['BC_xcqm_tkb_TF']))
# b = json.loads(str(a))

with open(file='test2.json',mode='w',encoding='utf-8') as f:
    json.dump(fp=f,obj=da_l,ensure_ascii=False,indent=4,separators=(',',':'))
# print(b)
# print(type(b))
