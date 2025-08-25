# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 22:37:37 2025

@author: Ikun
"""

import requests
import pandas as pd

linktable=pd.read_csv('linktable.csv')
links=linktable.iloc[:,0]
url="https://api.xiaoheihe.cn/bbs/app/link/tree"
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'connection': 'keep-alive',
    'cookie': 'user_pkey=MTc1NTk1NzUyMC43M183NjI2NDc2N3B3dWVrdGhydXFnbXNwdWg__; user_heybox_id=76264767; heybox_id=76264767; nickname=Ciallo%u5B66%u957F; avatar=https%3A//imgheybox.max-c.com/avatar/2025/03/28/6d65dadab5cbed00d18d1c0902b3302d.jpeg%3FimageMogr2/thumbnail/100x100%253E; level=10; wa=0; wr=0; ws=%5B%5D; wj=%5B%5D; wc=1; wiki_power=0; permission=0; ac=undefined; br=0; bes=%5B%5D; bea=%5B%5D; beb=%5B%5D; bms=%5B%5D; bma=%5B%5D; bmb=%5B%5D; fss=0; fsa=0; fsb=0; _ga=GA1.1.1622380397.1755957518; Hm_lvt_dfc8b88f31d0ba1cef80180022f4b3df=1755957472,1756040123; Hm_lpvt_dfc8b88f31d0ba1cef80180022f4b3df=1756040123; HMACCOUNT=7E937FA58B5AD871; _ga_DZ9BGTZW4G=GS2.1.s1756046337$o3$g1$t1756047776$j38$l0$h0; x_xhh_tokenid=BPq8pGlKefCMpCmqZIUrxLdkCqGnq6V/hA63qmKRtqZgg8gRCcNxP+ucgbLk08pO9gQ+Wm9zjY5OeNcOAKOd2Wg%3D%3D',
    'host': 'api.xiaoheihe.cn',
    'origin': 'https://www.xiaoheihe.cn',
    'referer': 'https://www.xiaoheihe.cn/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
}
for link in links:
    for i in range(1,3):
        params = {
            'os_type': 'web',
            'app': 'heybox',
            'client_type': 'web',
            'version': '999.0.4',
            'web_version': '2.5',
            'x_client_type': 'web',
            'x_app': 'heybox_website',
            'heybox_id': '76264767',
            'x_os_type': 'Windows',
            'device_info': 'Edge',
            'device_id': 'cde0c7d580878e4a4e52fb8dacc061b9',
            'hkey': 'IYYI225',
            '_time': '1756051840',
            'nonce': 'F5BD1578BB3D243A66CA6A54DFB8298A',
            'link_id': link,
            'is_first': '0',
            'page': i,
            'index': '1',
            'limit': '20',
            'owner_only': '0'
        }
        response=requests.get(url,params=params,headers=headers)
        with open(f'./网页/{link}_{i}.txt','w',encoding='utf-8') as fp:
            fp.write(response.text)