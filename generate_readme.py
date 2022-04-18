#! /usr/bin/env python3
# coding: utf-8
# @Author: Jor<jorhelp@qq.com>
# @Date: 2022年 4月18日 星期一 19时28分38秒 CST
# @Desc: 将 json 写进 README.md 文件

import os
import time
import json
import pyfiglet


def title() -> None:
    fig = pyfiglet.Figlet(font="graffiti")
    return f"```{fig.renderText('EDU Website')}```\n\n"


def header() -> str:
    info = ["```\n",
           f"@Author: Jorhelp<jorhelp@qq.com>\n",
           f"@Date: {time.asctime(time.localtime(time.time()))}\n",
           f"@Desc: 国内高校网址汇总，可以用来做数据分析或数据挖掘，甚至可以批量扫描来渗透测试(遵守法律，不要做出格的事)\n",
            "```\n\n"]
    return ''.join(info)


with open('edu.json', 'r') as f:
    jdata = json.load(f)


with open('README.md', 'w') as f:
    f.write(title())
    f.write(header())

    col_num = 5
    for province, vals in jdata.items():
        f.write(f"### {province}\n\n")
        f.write(f"> 总数: {len(vals)}\n\n")

        # 构造一个表格
        f.write('|' * (col_num + 1) + '\n')  # 共 5 列
        f.write('-'.join(['|'] * (col_num + 1)))
        _count = 0
        _tmp = '|'
        for name, url in vals.items():
            _tmp += f"[{name}]({url})|"
            _count += 1
            if _count == col_num:
                f.write(_tmp + '\n')
                _count = 0
                _tmp = '|'
        # 最后不够 col_num 的若干个
        if _count > 0:
            _tmp += '|' * (col_num - _count)
            f.write(_tmp + '\n')
            
        f.write('\n\n')
