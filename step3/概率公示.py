# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 10:26:59 2025

@author: Ikun
"""

import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

counttable=pd.read_csv('counttable.csv')
counttable = counttable[counttable['username'] != 'Ciallo学长']
sumCount=counttable['count'].sum()
counttable['rate']=counttable['count']/sumCount
rT=counttable
rT = rT.sort_values('count', ascending=False).reset_index(drop=True)
rT.to_csv('counttable.csv',index=False,encoding='utf-8')

# 创建饼图
plt.figure(figsize=(13.5, 10))

# 选择前44名用户显示，其余合并为"其他"
top_n = 44
top_users = rT.head(top_n)
other_rate = rT['rate'][top_n:].sum()

# 准备饼图数据
labels = list(top_users['username']) + ['其他']
sizes = list(top_users['rate']) + [other_rate]

# 创建饼图
wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# 美化标签
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# 添加标题
plt.title('用户获奖概率分布', fontsize=16, fontweight='bold')

# 确保饼图是圆形
plt.axis('equal')

# 添加图例
plt.legend(wedges, [f'{l}: {s:.2%}' for l, s in zip(labels, sizes)],
          title="用户及其概率",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# 显示图表
plt.tight_layout()
plt.show()

# 打印总概率信息
print(f"总参与次数: {sumCount}")
print(f"总用户数: {len(rT)}")
print(f"平均获奖概率: {(1/len(rT))*100:.4f}%")
print("\n用户获奖概率:")
for i, row in rT.iterrows():
    print(f"{i+1}. {row['username']}: {row['rate']*100:.2f}%")