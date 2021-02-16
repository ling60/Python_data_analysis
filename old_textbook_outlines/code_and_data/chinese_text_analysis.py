# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:06:54 2018

@author: ling
"""

import string
import jieba

# read text from a file

with open('data/world_cup_chinese.txt', encoding='utf8') as ff:
    footballtxt = ff.read()

## clean text: remove punctutation and tokenization words
#
## remove punctutation
## get punctutation

footballtxt = footballtxt.replace('\u3000', '')
football = ''.join([i for i in footballtxt if i not in string.punctuation])

## tokenization and lower cases

ftlst = jieba.lcut(footballtxt)


 # a better way to do it
from collections import Counter
counts = Counter(ftlst)
print(counts.most_common(30))
