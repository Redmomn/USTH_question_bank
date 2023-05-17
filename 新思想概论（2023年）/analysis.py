import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 原始json整理
def raw_json(filename):
    with open(file=filename,mode='r',encoding='utf-8') as f:
        a = json.load(fp=f) # 去除多余反斜杠
    b = a['text']
    b = json.loads(b) #去多余引号
    if 'BC_xcqm_tkb_SC' in b['BusinessData'].keys():
        return b['BusinessData']['BC_xcqm_tkb_SC'],0
    if 'BC_xcqm_tkb_MC' in b['BusinessData'].keys():
        return b['BusinessData']['BC_xcqm_tkb_MC'],1
    if 'BC_xcqm_tkb_TF' in b['BusinessData'].keys():
        return b['BusinessData']['BC_xcqm_tkb_TF'],2

# 没用
def sw_dict_to_list(filename):
    with open(file=filename,mode='r',encoding='utf-8') as f:
        a:dict = json.load(fp=f)
    if 'BC_xcqm_tkb_SC' in a['BusinessData'].keys():
        return a['BusinessData']['BC_xcqm_tkb_SC'],0
    if 'BC_xcqm_tkb_MC' in a['BusinessData'].keys():
        return a['BusinessData']['BC_xcqm_tkb_MC'],1
    if 'BC_xcqm_tkb_TF' in a['BusinessData'].keys():
        return a['BusinessData']['BC_xcqm_tkb_TF'],2

# 单选选项复选框
def SC_xxzh(i):
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

# 单选写入文件
def SC_md(title_list):
    mdfile = '单选.md'
    try:
        f = open(mdfile,mode='r',encoding='utf-8')
        f.close()
    except Exception:
        with open(mdfile,mode='w',encoding='utf-8'):
            pass
    with open(mdfile,mode='a',encoding='utf-8') as f:
        s = 1
        for i in title_list:
            if s>=99:
                s=1
            f.write(f"{s}. {i['wt']}\n") # 题目
            f.writelines(SC_xxzh(i))
            s+=1

# 多选选项复选框
def MC_xxzh(i):
    t_list=[]
    try:
        for j in range(1,10):
            te:str = i[f'xx{j}']
            for da in i['da']:
                stat = 0
                if te == '':
                    continue
                if te.startswith(da):
                    t_list.append(f'    - [x] {te}\n')
                    stat = 1
                    break
                # else:
                #     t_list.append(f'    - [ ] {te}\n')
                #     break
            if stat == 0 and te != '':
                t_list.append(f'    - [ ] {te}\n')
    except Exception:
        pass
    return t_list

# 多选写入文件
def MC_md(title_list):
    mdfile = '多选.md'
    try:
        f = open(mdfile,mode='r',encoding='utf-8')
        f.close()
    except Exception:
        with open(mdfile,mode='w',encoding='utf-8'):
            pass
    with open(mdfile,mode='a',encoding='utf-8') as f:
        s = 1
        for i in title_list:
            if s>=99:
                s=1
            f.write(f"{s}. {i['wt']}\n") # 题目
            f.writelines(MC_xxzh(i))
            s+=1

def main():
    title_list,tittle_type = raw_json('example.json')
    if tittle_type == 0:
        SC_md(title_list)
    if tittle_type == 1:
        MC_md(title_list)

if __name__ == '__main__':
    main()