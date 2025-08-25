# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 09:05:17 2025

@author: Ikun
"""
import re
import pandas as pd

linktable=pd.read_csv('linktable.csv')
links=linktable.iloc[:,0]
id_name=pd.DataFrame(columns=['userid','username'])
id_count=pd.DataFrame(columns=['userid','count'])
for link in links:
    userids=[]
    usernames=[]
    for i in range(1,3):
        with open(f'./网页/{link}_{i}.txt','r',encoding='utf-8') as fp:
            content=fp.read()
        userids.extend(re.findall('"userid":"(.*?)","username":".*?"', content, re.S))
        usernames.extend(re.findall('"userid":".*?","username":"(.*?)"', content, re.S))
    df=pd.DataFrame({
        'userid': userids,
        'username': usernames
    })
    df = df.drop_duplicates().reset_index(drop=True)
    id_name=pd.concat([id_name, df], ignore_index=True, sort=False).drop_duplicates().reset_index(drop=True)
    #id_times如果df出现useid则times+1，没有userid则新加入userid设times=1
    temp_df = pd.DataFrame({'userid': df['userid'], 'added': 1})
    temp_df = pd.merge(id_count, temp_df,on='userid',how='outer')#NaN 值替换为 0
    temp_df.fillna(0, inplace=True)
    temp_df['count'] = temp_df['added'] + temp_df['count']  # 计算新的 times 值
    id_count = temp_df[['userid', 'count']]
id_name.to_csv('id_name.csv', index=False, encoding='utf-8')
counttable=pd.merge(id_name, id_count,on='userid',how='outer')
counttable.to_csv('../step3/counttable.csv',index=False,encoding='utf-8')