# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 20:46:41 2025

@author: Ikun
"""

import re
import pandas as pd

with open('./主页.html','r',encoding='utf-8') as fp:
    content=fp.read()
   
links=re.findall('<a href="/app/bbs/link/(.*?)".*?<div class="bbs-content__title">.*?<',content,re.S)
titles=re.findall('<a href="/app/bbs/link/.*?".*?<div class="bbs-content__title">(.*?)<',content,re.S)

df = pd.DataFrame({
    'links': links,
    'titles': titles
})
df = df[df['titles'].str.contains('基金|fund', case=False, na=False)].drop(70)
df = df.reset_index(drop=True)

print(df)
df.to_csv('../step2/linktable.csv', index=False, encoding='utf-8')
