#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:44:27 2023

@author: jaishree
"""

import pandas as pd
#import numpy as np
import re
df=pd.read_csv('/Users/jaishree/Downloads/datasets[47]/final_perfume_data.csv',encoding='unicode_escape')
df.drop(columns=['Image URL'],inplace=True)
df['Notes'].fillna('',inplace=True)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_mat = tfidf.fit_transform(df['Notes'])
#tfidf_mat
from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_mat,tfidf_mat)
#cosine_sim

data = pd.Series(df['Notes'],index = df.index)
data = pd.DataFrame(data)
#data
'''
def recommendation(keyword):
    index = data[data['Notes'].str.contains(keyword, flags=re.IGNORECASE, regex=True)].index[0]
    sim_score = list(enumerate(cosine_sim[index]))    
    sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
    
    sim_score = sim_score[1:8]
    final_index = [i[0] for i in sim_score]
    return final_index
rec=str(input("Enter a flavour for recommendation : "))
idx=recommendation(rec)

print("\nRecommended Perfumes are : \n")
for i in idx:
    print('--> ',df['Name'][i])
df['Notes'].iloc[idx].str.contains(rec,flags=re.IGNORECASE, regex=True)
'''
class Recommendation:
    def __init__(self):
        self.data=data
        self.cosine_sim=cosine_sim
    def recommendation(self,x):
        ind=self.data[data['Notes'].str.contains(x,flags=re.IGNORECASE,regex=True)].index[0]
        sim_score=list(enumerate(self.cosine_sim[ind]))
        sim_score=sorted(sim_score,key=lambda a:a[1],reverse=True)
        sim_score=sim_score[1:8]
        final_ind=[i[0] for i in sim_score]
        return final_ind
    def predict(self,x):
        l1=pd.DataFrame()
        ind=self.recommendation(x)
        l1['Name']=df['Name'].iloc[ind]
        #l1['rating']=df['rating'].iloc[ind]
        #l1['url']=df['url'].iloc[ind]
        return l1
        
        


import pickle
rec=Recommendation()
print(rec.predict('rose'))
pickle.dump(rec,open('model.pkl','wb'))
