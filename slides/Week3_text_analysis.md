# Python For Data Science

## Lecture 3, data collection & text analysis

今天的课程里，我们主要介绍以下几个方面的内容：

1. 数据分析的流程介绍
2. 数据清理：文本分析和量化

## Data analysis processs

1. Problem Define
2. Data collection
3. Data cleaning
4. Modelling
5. Report


### 模型需要的数据类型

**Level of Measurement**

- Nomial/Categorical
    - 定类，1-male，2-female
- Ordinal
    - 定序，1，完全同意；2，基本同意...
- Interval
    - 定距，0没有实在意义，温度
- Ratio
    - 定比，身高，体重

## Data Cleaning -- NLP

### NLP

Natural language processing (NLP) is a field of [computer science](https://en.wikipedia.org/wiki/Computer_science), [artificial intelligence](https://en.wikipedia.org/wiki/Computational_linguistics) and computational linguistics concerned with the interactions between  computers and [human (natural) languages](https://en.wikipedia.org/wiki/Natural_language)


### Main aims of NLP

1. Information Retrieval
2. Text Quantification
3. Machine Translation
4 ...

#### Query Relevance

- 文本相关性
    * 与所提供的关键词的相关性
- “人工智能的应用”


#### 流程

“人工智能的应用”

1. 分词: 
    - 人工智能, 的, 应用
2. 如何判断一篇文章和这几个词的相似度?
    - 相关文本出现次数
3. 含有这三个词的数量是否越多越好?
    - 词频(term frequency)
4. 相关性（相似度）
    - 一个查询语句包含N个关键词:W1, W2, …WN
    - 出现在一篇文章/网页里的词频是:TF1, TF2…TFN
    - 那么这个查询语句与这个网页的相关性就是:
    - TF1+ TF2+…TFN
5. 问题？
   - 有一些无意义的词,比如”的”
        * stopwords
    - 去掉”的”是否合适?
    - “人工智能”和”应用”是否应等同对待?
        * 加权重,如何设置?
6. 一个好办法：TF-IDF

#### Information Retrieval References

1. 数学之美--吴军
2. Stanford University, Information Retrieval and Web Search (CS276)


**经管领域常见文本分析技术和应用**

- 分词-stemming,tokenization
- 词频-term frequency
- 信息提取-entity extraction

* 文本相似度-Text similarity
* 相关性-Text relevance
* 主题分类-topic classification


### Text Quantification

### 一个最简单的情感分析

我们了解到要想做一个最简单的情感分析，比如，分析下面这句话的情感（计算情感分值），我们需要如下的步骤：

```
'We have some delightful new food in the cafeteria. Awesome!!!!'
```

1. 将上面这句话赋值给一个string类型的变量，sentence
2. 获得（建立）积极消极情感词表（两个list,positive_words, negative_words）
3. 判断sentnce中每个词是否属于积极或消极情感词
4. 计算情感分值（# of 正面情感词/# of 所有词 – # of 负面情感词/# of 所有词）

### 情感分析

- 不止情感，还包括看法、意见等等
- 不止积极、消极

Some References：

- Bollen, J., Mao, H., & Zeng, X. (2011). Twitter mood predicts the stock market. Journal of Computational Science, 2(1), 1–8. article.
- Tetlock, P. C., Saar-Tsechansky, M., & Macskassy, S. (2008). More than words: Quantifying language to measure firms’ fundamentals. The Journal of Finance, LXIII(3), 1437–1467.
 
- Bing Liu的 Sentiment Analysis and Opinion Mining Morgan & Claypool Publishers
- Bo Pang的 Opinion Mining and Sentiment Analysis


### 语料库

**语料库列表：**
- List of text corpora: https://en.wikipedia.org/wiki/List_of_text_corpora

**国外常见语料库**
- Oxford BNC: http://www.natcorp.ox.ac.uk/
- Pitt Uni: http://mpqa.cs.pitt.edu/
- Stanford: https://nlp.stanford.edu/projects/snli/

**国内常见语料库**
- 清华：http://thuocl.thunlp.org/
- 哈工大：http://ir.hit.edu.cn/


### References

- Bollen, J., Mao, H., & Zeng, X. (2011). Twitter mood predicts the stock market. Journal of Computational Science, 2(1), 1–8. article.（计科方向）
- Tetlock, P. C., Saar-Tsechansky, M., & Macskassy, S. (2008). More than words: Quantifying language to measure firms’ fundamentals. The Journal of Finance, LXIII(3), 1437–1467 （金融向）
- Bing Liu的 Sentiment Analysis and Opinion Mining Morgan & Claypool Publishers
- Bo Pang的 Opinion Mining and Sentiment Analysis


文本分析的一些相关介绍：

1. https://www.wonderflow.co/blog/text-analysis
2. https://monkeylearn.com/text-analysis/


### Another approach

[word embedding](https://en.wikipedia.org/wiki/Word_embedding)

- 词向量，词嵌入
- word2vec, 
- Bert,from [Google](https://blog.google/products/search/search-language-understanding-bert/)
- GPT-3,from [OpenAI](https://openai.com/blog/openai-api/)

A related package:
[Gensim](https://radimrehurek.com/gensim/)

当前有很多训练好的开源word vector的模型供大家下载，比如fasttext等

可以用如下方法对这些model进行调用，甚至是“更新”。具体参见：
https://radimrehurek.com/gensim/models/keyedvectors.html


```python
from gensim.test.utils import datapath

wv_from_text = KeyedVectors.load_word2vec_format('w2v_model/wiki-news-300d-1M.vec')
```


```python
wv_from_text.most_similar(positive=['woman', 'king'], negative=['man'])
```
