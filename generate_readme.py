#! /usr/bin/env python3
# coding: utf-8
# @Author: Jor<jorhelp@qq.com>
# @Date: 2022年 4月18日 星期一 19时28分38秒 CST
# @Desc: 将 json 写进 README.md 文件

import json


with open('edu.json', 'r') as f:
    jdata = json.load(f)


with open('README.md', 'w') as f:
    for province, vals in jdata.items():
        #  print(province, len(vals))
        f.write(f"### {province}\n")
        for name, url in vals.items():
            f.write(f"[{name}]({url})  ")
        f.write('\n')
