import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 原始json整理
def raw_json(filename):
    with open(file=filename,mode='r',encoding='utf-8') as f:
        a = json.load(fp=f) # 去除多余反斜杠
    b = a['text']
    b = json.loads(b) #去多余引号
    return b['BusinessData']['BC_xcqm_tkb_SC']

def sw_dict_to_list(filename):
    with open(file=filename,mode='r',encoding='utf-8') as f:
        a = json.load(fp=f)
    return a['BusinessData']['BC_xcqm_tkb_SC']

# 选项复选框
def xxzh(i):
    t_list=[]
    try:
        for j in range(1,10):
            te:str = i[f'xx{j}']
            if te == '':
                continue
            if te.startswith(i['da']):
                t_list.append(f'    - [x] {te}\n')
            else:
                t_list.append(f'    - [ ] {te}\n')
    except Exception:
        pass
    return t_list

title_list = raw_json('单选.json')
mdfile = '单选.md'
try:
    f = open(mdfile,mode='r',encoding='utf-8')
    f.close()
except Exception:
    with open(mdfile,mode='w',encoding='utf-8'):
        pass
with open(mdfile,mode='a',encoding='utf-8') as f:
    for i in title_list:
        f.write(f"{i['xh']}. {i['wt']}\n") # 题目
        f.writelines(xxzh(i))
