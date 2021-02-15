# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:40:43 2018

@author: Ling
"""

# 文件读取
with open('data/deep_learning.txt', encoding='utf8') as ff:
    deeptxt = ff.read()
    
    
# 文本清理： 分词，去除标点
import string
text = ''.join([i.lower() for i in deeptxt if i not in string.punctuation])
words = text.split()

# 数词频
wordic = dict()
for word in words:
    if word in wordic:
        wordic[word] = wordic[word] + 1
    else:
        wordic[word] = 1

wordslst = list(wordic.items())
wordslst.sort(key=lambda x:x[1], reverse=True)