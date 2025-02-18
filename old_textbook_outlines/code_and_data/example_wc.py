# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:50:36 2016

@author: ling
"""

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

#from os import path
from wordcloud import WordCloud

# Read the whole text.
text = open(r'data/obama_tweets.txt').read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(width=800, height=400, max_font_size=40, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


