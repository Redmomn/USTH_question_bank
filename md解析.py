# 快速解析题库至docs文件夹

import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# json文件存放的路径，末尾加上/
filePath = "./raw_json/新思想（2023）/"

# 输出的md文件存放的路径，末尾加上/
outFilePath = "./docs/1033新思想概论（2023年）/"

# 课程名称
courseName = "新思想概论（2023年）"

jsonFileList = ["单选.json", "多选.json", "判断.json"]
mdFileList = ["单选.md", "多选.md", "判断.md"]


# 原始json整理
def raw_json(filename):
    with open(file=filename, mode="r", encoding="utf-8") as f:
        a = json.load(fp=f)  # 去除多余反斜杠
    b = a["text"]
    b = json.loads(b)  # 去多余引号
    if "BC_xcqm_tkb_SC" in b["BusinessData"].keys():
        return b["BusinessData"]["BC_xcqm_tkb_SC"], 0
    if "BC_xcqm_tkb_MC" in b["BusinessData"].keys():
        return b["BusinessData"]["BC_xcqm_tkb_MC"], 1
    if "BC_xcqm_tkb_TF" in b["BusinessData"].keys():
        return b["BusinessData"]["BC_xcqm_tkb_TF"], 2


# 没用
def sw_dict_to_list(filename):
    with open(file=filename, mode="r", encoding="utf-8") as f:
        a: dict = json.load(fp=f)
    if "BC_xcqm_tkb_SC" in a["BusinessData"].keys():
        return a["BusinessData"]["BC_xcqm_tkb_SC"], 0
    if "BC_xcqm_tkb_MC" in a["BusinessData"].keys():
        return a["BusinessData"]["BC_xcqm_tkb_MC"], 1
    if "BC_xcqm_tkb_TF" in a["BusinessData"].keys():
        return a["BusinessData"]["BC_xcqm_tkb_TF"], 2


# 单选选项复选框
def SC_xxzh(i):
    t_list = []
    try:
        for j in range(1, 10):
            te: str = i[f"xx{j}"]
            if te == "":
                continue
            if te.startswith(i["da"]):
                t_list.append(f"    - [x] {te}\n")
            else:
                t_list.append(f"    - [ ] {te}\n")
    except Exception:
        pass
    return t_list


# 单选写入文件
def SC_md(title_list):
    mdfile = outFilePath + "单选.md"
    try:
        f = open(mdfile, mode="w", encoding="utf-8")
        f.close()
    except Exception:
        with open(mdfile, mode="w", encoding="utf-8"):
            pass
    with open(mdfile, mode="a", encoding="utf-8") as f:
        s = 1
        for i in title_list:
            # if s >= 99:
            #     s = 1
            f.write(f"{s}. {i['wt']}\n")  # 题目
            f.writelines(SC_xxzh(i))
            s += 1


# 多选选项复选框
def MC_xxzh(i):
    t_list = []
    try:
        for j in range(1, 10):
            te: str = i[f"xx{j}"]
            for da in i["da"]:
                stat = 0
                if te == "":
                    continue
                if te.startswith(da):
                    t_list.append(f"    - [x] {te}\n")
                    stat = 1
                    break
                # else:
                #     t_list.append(f'    - [ ] {te}\n')
                #     break
            if stat == 0 and te != "":
                t_list.append(f"    - [ ] {te}\n")
    except Exception:
        pass
    return t_list


# 多选写入文件
def MC_md(title_list):
    mdfile = outFilePath + "多选.md"
    try:
        f = open(mdfile, mode="w", encoding="utf-8")
        f.close()
    except Exception:
        with open(mdfile, mode="w", encoding="utf-8"):
            pass
    with open(mdfile, mode="a", encoding="utf-8") as f:
        s = 1
        for i in title_list:
            # if s >= 99:
            #     s = 1
            f.write(f"{s}. {i['wt']}\n")  # 题目
            f.writelines(MC_xxzh(i))
            s += 1


# 多选复选框
def TF_xxzh(i):
    t_list = []
    try:
        if i["da"] == "对":
            t_list.append("    - [x] 对\n")
            t_list.append("    - [ ] 错\n")
        else:
            t_list.append("    - [ ] 对\n")
            t_list.append("    - [x] 错\n")
    except Exception:
        pass
    return t_list


# 判断写入文件
def TF_md(title_list):
    mdfile = outFilePath + "判断.md"
    try:
        f = open(mdfile, mode="w", encoding="utf-8")
        f.close()
    except Exception:
        with open(mdfile, mode="w", encoding="utf-8"):
            pass
    with open(mdfile, mode="a", encoding="utf-8") as f:
        s = 1
        for i in title_list:
            # if s >= 99:
            #     s = 1
            f.write(f"{s}. {i['wt']}\n")  # 题目
            f.writelines(TF_xxzh(i))
            s += 1


def main():
    ### 转换md
    for fileName in jsonFileList:
        title_list, tittle_type = raw_json(filePath + fileName)
        if tittle_type == 0:
            SC_md(title_list)

        if tittle_type == 1:
            MC_md(title_list)

        if tittle_type == 2:
            TF_md(title_list)

    for fileName in mdFileList:
        if os.path.exists(outFilePath + fileName):
            pass
        else:
            return 0

    with open(
        file=f"{outFilePath}/{courseName}.md", mode="w", encoding="utf-8"
    ) as file:
        file.write(f"# {courseName}\n\n")

        # 单选题目
        file.write("## 单选\n\n")
        with open(
            file=f"{outFilePath}/{mdFileList[0]}", mode="r", encoding="utf-8"
        ) as f:
            file.write(f.read())

        # 多选题目
        file.write("## 多选\n\n")
        with open(
            file=f"{outFilePath}/{mdFileList[1]}", mode="r", encoding="utf-8"
        ) as f:
            file.write(f.read())

        # 判断题目
        file.write("## 判断\n\n")
        with open(
            file=f"{outFilePath}/{mdFileList[2]}", mode="r", encoding="utf-8"
        ) as f:
            file.write(f.read())

    for fileName in mdFileList:
        os.remove(outFilePath + fileName)


if __name__ == "__main__":
    main()
