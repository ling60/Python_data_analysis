# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 16:38:42 2018

@author: ling
"""
import string

# read text from a file

with open('data/deep_learning.txt', encoding='utf8') as ff:
    deeptxt = ff.read()

# clean text: remove punctutation and tokenization words

# remove punctutation
# get punctutation

deepnopun = ''.join([i for i in deeptxt if i not in string.punctuation])

# tokenization and lower cases
deep = deepnopun.lower().split()

# cal word frequency

wordcount = dict()

for word in set(deep):
    wordcount[word] = 0
for w in deep:
    wordcount[w] += 1

wordcountlst = list(wordcount.items())
wordcountlst.sort(key= lambda x:x[1], reverse=True
)

# a better way to do it
from collections import Counter
counts = Counter(deep)
print(counts.most_common(30))
