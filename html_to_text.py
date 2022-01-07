# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:48:11 2021

@author: emreb
Yerel haberlerde     son 3

"""

import requests
from nltk import tokenize
from bs4 import BeautifulSoup
import functions as f
import sqlite_functions as sql

import pandas as pd



data = sql.takeSentence("sentences.db", "yazarlar_11")
links = list()
sentences = list()
for  i in range(0,len(data)):
    links.append(data[i][0])
    
news= 0    

for  i in links:
    news = news + 1
   
     
    html = requests.get(i).text
    soup = BeautifulSoup(html)  
    
    text = soup.get_text("\n")
    nonfilter_sentence = tokenize.sent_tokenize(text)
    for j in range(0,len(nonfilter_sentence)):
        adding , sentence = f.filter_sentence(nonfilter_sentence[j])
        
        if adding:
            sentences.append(sentence)

    if news%100 == 0 :
        print("Number of news:",news,"Total sentence:",len(sentences))


sentences = f.unique(sentences)
temp_sent = list()
for i in range(0,len(sentences)):
    temp_sent.append(sentences[i][0])
    
    
sentences_df = pd.DataFrame(data=sentences)
sentences_df.to_csv("Sentences_11.csv")
    
    

    
    
    