
# coding: utf-8

# In[ ]:


import bs4 as bs
import sys
import codecs
import nltk
import urllib.request
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
import re


class ScrapeData(object):
    def __init__(self):
        pass
    #for parsing the url link and extracting the text currently form p tags
    def urlparser(self,url):
        sourceurl = urllib.request.urlopen(url).read()
        #using the xml parser and have options like html
        data = bs.BeautifulSoup(sourceurl,'lxml')
        fr=[]
        for pdata in data.find_all('p'):       
            fr.append(pdata.text)
        fr_str=''.join(fr)
        return fr_str
    #for counting number of occurence of words in the webpage
    def count_frequency(self,input_string):
        e_str=input_string.split()        
        c=Counter(e_str)
        for k in c:
            print(k,c[k])
    #tokenization of words
    def tokenize_clean(self,data):  
        data = re.sub("[^a-zA-Z0-9]"," ",data)
        #word tokenization
        word_tokenized_list= word_tokenize(data)        
        words = [word for word in word_tokenized_list if len(word) > 1]        
        # for making words in to lower case
        words = [word.lower() for word in word_tokenized_list]        
        # by making stopwords to default english setting
        english_stopwords = set(nltk.corpus.stopwords.words('english'))
        #remove stop words
        words = [word for word in word_tokenized_list if word not in english_stopwords]
        return words
    #word frequency plot
    def visualize(self,data_list):
        word_dist = nltk.FreqDist(data_list)
        plt.figure(figsize=(12,6))
        word_dist.plot(60)
        
     #for counting words
    def word_count(self,dataa_list):
        count = dict()
        words = dataa_list.split()
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        return count
        
if __name__=="__main__":
    ssd=ScrapeData()
    scraped_data=ssd.urlparser('http://mccormickml.com/2016/11/08/dbscan-clustering/')
    ssd.count_frequency(scraped_data)
    tokenized_word_list=ssd.tokenize_clean(scraped_data)
    ssd.visualize(tokenized_word_list)
    #for writing words in to csv file
    word_list=ssd.word_count(scraped_data)
    with open('word_freqfile.csv', 'w') as f: 
        wf = csv.writer(f)
        wf.writerows(word_list.items())
      
#date format logic
#date format checker second solution
import time
import datetime
import numpy
import pandas as pd
import csv
import re

outPutDateFormat = "%d/%m/%Y"
datesample = pd.read_csv('set2.csv')
dateslist = datesample["words"].values.astype(str).tolist()
    


def check_format(datec):    
    format_ok = False
    for mask in ['%Y%m%d','%Y-%m-%d','%d-%m-%Y','%m%d%Y','%A, %d, %B, %y','%d%m-%Y','%Y/%m/%d','%m/%d/%Y','%d/%m/%Y']:
        try:
            time.strptime(datec, mask)
            format_ok = True
            break
        except ValueError:
            pass
    if format_ok:
        date0=datetime.datetime.strptime(datec ,mask)
        date1=datetime.date.strftime(date0, outPutDateFormat)
        return date1
    else:
        return "incorrect date format" 
    return None
 
def main():
    RE = r"(\d{1,2})(\/)*(\d{1,2})(\/)*(\d{2,4})"
    f = open('datecorrections.csv', 'w')
    datelist=[]
    List_RE=['RE']
    for date in dateslist:       
        for pattern in List_RE:
            regex = re.compile(eval(pattern))
            m = regex.finditer(date)
            if m :
                for m1 in m:
                    datelist.append(m1.group(0))
    #print(datelist)
    f = open('datecorrections.csv', 'w')
    for date in datelist:
        wf = csv.writer(f)
        wf.writerow([date,check_format(date)])
        

if __name__=="__main__":
    main()


#label checker
import pandas as pd
import csv

#reading the data
categories=['B-return_date','O']
datesample = pd.read_csv('set2.csv')
dateslist = datesample["labels"].values.astype(str).tolist()

#lgc
def returnMatches(a,b):
    if a in b:
        return a
    else:
        return "No match"
f = open('datecorrections.csv', 'w')
for date in dateslist:
    wf = csv.writer(f)
    wf.writerow([date,returnMatches(date,categories)])

#if __name__=="__main__":
returnMatches(categories,dateslist)
