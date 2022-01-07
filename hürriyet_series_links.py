# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 23:51:16 2021

@author: emreb
"""

from selenium import webdriver
import sqlite_functions as sql
import time
import functions as f
import pandas as pd 

year = ["2011"]
driver = webdriver.Firefox()   
link = list()
for k in range(0,len(year)):
    for i in range(1,1000):    
        links = list()
        url = "https://www.hurriyet.com.tr/arama/#/?page="+str(i)+"&order=Yeniden%20Eskiye&where=/yazarlar/&how=Column&year="+year[k]+"&platform=/yazarlar/&isDetail=true"

        driver.get(url)
        try:
           time.sleep(2)
           elems= driver.find_elements_by_css_selector(".hs-cnn-content [href]")
           links = [elem.get_attribute('href') for elem in elems]
        except:
            links = list()
            pass
        for j in links:
          if len(j) > 50 and f.filter_links(j):
             link.append(j)
        if i%100 == 0:
             print("Page:",i," Year:" + year[k]+" # link:",len(link)) 


link = f.unique(link)
link_df = pd.DataFrame(data=link)
link_df.to_csv("yazarlar_11.csv")