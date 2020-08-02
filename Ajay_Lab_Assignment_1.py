import pandas as pd
import os
import nltk
import re
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
path = r'C:\Users\AJAY\Documents\CURAJ\IR\reuters'
path_Stop_Word = r'C:\Users\AJAY\Documents\CURAJ\IR\stop_words.csv'

''''
  In this stop word file i add some more stop words
  these stop words are single character basically.
'''
def get_Stop_Words(path_Stop_Word):
  with open(path_Stop_Word,'r') as f:
    stop_Words=f.read()
  return stop_Words.split("\n")



def get_Doc(path):
  '''
    This fuction take path directory and 
    return all the files with '.sgm' extension.
  '''
  files = os.listdir(path)
  text_files = list()
  for x in files:
    if x.endswith('.sgm'):
      text_files.append(x)
  return text_files

def get_Doc_Content(path):
  '''
    This fuction is use get_Doc() fuction for
    geting files and converting file content
    into list of all document content.
  '''
  doc_file= list()
  for doc in get_Doc(path):
    contant = "".join([path+'\\'+doc])
    with open(contant,'r') as f:
      doc_file.append(f.read())
      f.close()
  return doc_file



def stop_Words(token):
  stop_Words = get_Stop_Words(path_Stop_Word)
  # print(stop_Words)
  token_Remove_Stop_Words = list()
  for doc in token:
    temp = [word for word in doc if word not in stop_Words]
    token_Remove_Stop_Words.append(temp)
  return token_Remove_Stop_Words
  

def tokenization(path):
  '''
      This fuction is use get_Doc_Content() fuction for
      geting list of all document content and then performing 
      tokenization,only deals with [a-z0-9] character,digit.
      using regular expression,and its use stop_Words() fuction
      for remove stop words.
  '''
  token = list()
  doc_file = get_Doc_Content(path)
  for i,x in enumerate(doc_file):
    doc_file[i] = x.lower()
    # doc_file[i] = re.sub("[^a-z0-9]+"," ",doc_file[i])
    doc_file[i] = re.sub("[^a-z]+"," ",doc_file[i])
    doc_file[i] = doc_file[i].split()
    token.append(doc_file[i])
  '''
    convert frequence of term/token
  '''
  token_Remove_Stop_Words = stop_Words(token)
  freq_token = list()
  for x in token_Remove_Stop_Words:
    term = list(set(x))
    for j in term:
      freq_token.append((j,x.count(j)))
    # print(freq_token)    
  return token_Remove_Stop_Words,freq_token

def stemming(path):
  token_Remove_Stop_Words,freq_token = tokenization(path)
  # print("token",token_Remove_Stop_Words[0])
  porter = PorterStemmer()
  corpus = list()
  for words in token_Remove_Stop_Words:
    # corpus.append([porter.stem(term) for term in words])
    corpus.append(set([porter.stem(term) for term in words]))
  print("Corpus:",len(corpus[0]))
  return corpus

stemming(path)

  