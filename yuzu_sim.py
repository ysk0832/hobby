# -*- coding: utf-8 -*-


# google colab
# python3.6.8

import numpy as np 
import pandas as pd

# csv読み込み
df=pd.read_csv("cg.csv")

# 平均
mean=df.mean(numeric_only=True)
print(mean)

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

# 計算結果をリストに保存
simlist=[]
for i in range(0,186):
  result=sim(mean,df.iloc[i,1:6])
  print(result)
  simlist.append(result)

# 列を追加
df["類似度"]=simlist

# 類似度が高い順に出力
print(df.sort_values("類似度",ascending=False))

# 一旦削除
df=df.drop("類似度",axis=1)

# 正規化して再計算

# 名前抜き
df_tmp=df.iloc[:,1:6]
df_tmp

# 正規化
df2=(df_tmp-df_tmp.min())/(df_tmp.max()-df_tmp.min())
mean2=(mean-df_tmp.min())/(df_tmp.max()-df_tmp.min())
mean2

# 計算結果をリストに保存
simlist=[]
for i in range(0,186):
  result=sim(mean2,df2.iloc[i,:])
  print(result)
  simlist.append(result)

# 列を追加
df["類似度"]=simlist

# 類似度が高い順に出力
print(df.sort_values("類似度",ascending=False))

df=df.drop("類似度",axis=1)

# 平均値との距離
dlist=[]
for i in range(0,186):
  d=norm(df.iloc[i,1:6]-mean)
  dlist.append(d)

# 列を追加
df["距離"]=dlist
df

# 距離が近い順に出力
print(df.sort_values("距離"))

