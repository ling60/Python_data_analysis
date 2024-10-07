# encoding: utf-8
# by Kennis Yu/Ling Liu

from itertools import combinations
from collections import Counter
import os
import codecs
import re
from numpy import array, sqrt, square, sum


def clean(text):
    '''
    clean text.
    '''
    return re.sub('\W', ' ', text)


def createFullDict(full_word_set):
    '''
    return a dict including full words as its keys.
    '''
    return dict.fromkeys(full_word_set, 0)


def tokensize(text):
    '''
    tokensize the text into a word vetctor.
    '''
    return list(filter(lambda x: len(x) >= 2, text.strip().split()))


def count(word_set):
    '''
    return a dict like {word: count}.
    '''
    return Counter(word_set)


def fill(full_word_count_dict, word_count_dict):
    '''
    fill the full word count dict with the values from a specific word count dict.
    '''
    full_word_count_dict.update(word_count_dict)
    return array(list(full_word_count_dict.values()), dtype=float)


def calcSim(arr_a, arr_b):
    '''
    calculate the approximate distance by cosine.
    '''
    return sum((arr_a * arr_b)) / sqrt(sum(square(arr_a)) * sum(square(arr_b)))


def read(filename):
    '''
    read the file into a string.
    '''
    try:
        with codecs.open(filename, mode='r', encoding='utf-8') as fr:
            return fr.read()
    except UnicodeError:
        with codecs.open(filename, mode='r', encoding='gb18030') as fr:
            return fr.read()


def accessFiles(path):
    '''
    :path: <sting> the address of a python source collection.
    access the files and split them into words.
    '''
    words_collection = {}
    for f in os.listdir(path):
        abs_path = os.path.join(path, f)
        if not os.path.isfile(abs_path) or not f.endswith('.ipynb'):
            continue
        text = read(abs_path)
        cleaned_text = clean(text)
        words = tokensize(cleaned_text)
        words_collection[f] = words
    return words_collection


def structurize(words_collection):
    '''
    :words_collection: <dict> like {filename: [word1, word2, ...]}
    turn words into word vectors.
    '''
    full_word_ls = []

    for words in words_collection.values():
        full_word_ls.extend(words)
    full_word_set = set(full_word_ls)
    full_word_dict = createFullDict(full_word_set)
    # print(words_collection)
    word_count_collection = {}
    for f in words_collection:
        word_count_collection[f] = fill(
            full_word_dict.copy(), count(words_collection[f]))

    return word_count_collection


MIN_COS_DIST = 0.9


def isDuplicate(path):
    '''
    :path: <sting> the address of a python source collection.
    return the two filenames whoes cosine approximate distance >= 0.9.
    '''
    duplicate_set = []
    words_collection = accessFiles(path)
    word_count_collection = structurize(words_collection)
    for pair in combinations(word_count_collection.keys(), 2):
        calnum = calcSim(
            word_count_collection[pair[0]], word_count_collection[pair[1]])
        if calcSim(word_count_collection[pair[0]], word_count_collection[pair[1]]) >= MIN_COS_DIST:
            print(u"{}: {}".format(*pair), calnum)
            duplicate_set.append(pair)
    return duplicate_set


if __name__ == '__main__':
    path = u'pyfiles'
    duplicate_set = isDuplicate(path)
