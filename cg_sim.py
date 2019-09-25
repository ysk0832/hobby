# -*- coding: utf-8 -*-


# !python --version
# Python 3.6.8

import numpy as np
import pandas as pd

# csv読み込み
df=pd.read_csv("cg.csv")

# 内積
def ip(a,b):
  return (a*b).sum()
# ノルム
def norm(x):
  sum=(x*x).sum()
  return np.sqrt(sum)
# 類似度
def sim(a,b):
  return ip(a,b)/(norm(a)*norm(b))

# 名前と計算結果をリストに保存
name1list=[]
name2list=[]
simlist=[]
count = 0 #計算の進捗確認用
for i in range(0,185):
  for j in range(i+1,186):
    result=sim(df.iloc[i,1:6],df.iloc[j,1:6])
    count+=1
    if count%1000==0:
      print(result)
    name1list.append(df.iloc[i,0])
    name2list.append(df.iloc[j,0])
    simlist.append(result)

# 新たにデータフレームを作成
df_result=pd.DataFrame({'name1':name1list, 'name2':name2list, 'sim':simlist})

# 類似度top10を出力
print(df_result.sort_values("sim",ascending=False).iloc[0:10])

