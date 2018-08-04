
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
        
if __name__=="__main__":
    ssd=ScrapeData()
    scraped_data=ssd.urlparser('name of the url')
    ssd.count_frequency(scraped_data)
    tokenized_word_list=ssd.tokenize_clean(scraped_data)
    ssd.visualize(tokenized_word_list)
        

