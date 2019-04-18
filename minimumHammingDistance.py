import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv("sample.csv",names=['word' , 'bin'])


min = 1000000000000000000;
count = 1;
row_size = df.shape[0] # row의 개수
for i in range(row_size):
    for j in range(i+1,row_size) :
        hd = hamming(df.iloc[i,1], df.iloc[j,1]);
        print(count,"(",df.iloc[i,0], df.iloc[j,0],") hamming_distance: ",hd)
        count = count+1;
        if (hd < min):
            min = hd

# 행 전체 돌면서 자신이 아닌 것들로 비교해서 계산


print("min hamming distance", min)
