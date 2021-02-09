# Python For Data Science

## Lecture 4, Data access, data types, function, file RW

这次课主要内容是介绍在数据分析中，提出问题和数据获取的两个方面。同时还会介绍Python的一些基础数据类型。

## Data analysis processs

1. Problem Define
2. Data collection
3. Data cleaning
4. Modelling
5. Report


### Problem

在提出问题的过程中，可以参考以下几个方面：

1. 自己的兴趣、专业
2. 未来工作导向

提出问题时需要注意：

1. 问题范围太大
2. 实际应用范围过小
3. 项目完成可行性


问题的意义最重要

- 趣味性
- 价值
- 贡献
- 实际应用、理论贡献

几个常见数据科学方向的竞赛（需要注意，这些比赛都更注重算法）



如果需要查找相关文献，可使用学术搜索直接查询关键词：

1. [Google Scholar](https://scholar.google/)
2. [MS academic](https://academic.microsoft.com/home)
3. [Bing academic](https://www.bing.com/academic/)

## Data collection

- 数据来源非常重要
    - 优先：政府、高校、研究所等官方数据
    - 不要轻信网上提供的数据

- Data access and data cleaning are the most important processes in data analysis

- Garbage in, Garbage out


### Data access schemes

1. Bulk downloads
    - Wikipedia, IMDb, Million Song Database, etc
2. API access
    - NY Times, Twitter, Facebook，Google…
3. Web scraping


### 一些开放数据源的整理和集合

1. 复旦：中国开放数林指数报告

http://ifopendata.fudan.edu.cn/report

2. 探码科技

http://www.tanmer.com/blog/451

3. 网络上个人总结/整理

https://supergis.gitbooks.io/git_notebook/content/doc/opendatasource.html


### 国内数据集

- 各政府公共数据开放平台
    - 成都：http://www.cddata.gov.cn/oportal/index
    - 统计局：https://data.stats.gov.cn/
- 学校图书馆
- 国内财经数据接口package：http://tushare.org/


### 国外数据集

- Bulk download
    -Baron Schwartz's list of datasets. Some of these are themselves rich lists of datasets, such as the Amazon AWS public data sets.
    - Data.gov, U.S. open government data: data.wa.gov, Washington state open government data

- API
    - R datasets from github: http://vincentarelbundock.github.io/Rdatasets/datasets.html
    - BLS(美国统计局): http://www.bls.gov/data/#api

- Python packages

    - Statsmodel’s data access: http://statsmodels.sourceforge.net/stable/datasets/index.html
    - pandas remote data access: https://github.com/pydata/pandas-datareader

## Data Collection


网络爬虫本质上就是：用程序“模拟”人类浏览网页的状态

流程：

1. 判断网络URL
2. “下载”网页的内容或文件：requests
3. 解析网页：BeautifulSoup
4. 数据清理

常用的Python包：

#### Useful Packages

* *Requests*: download files and web pages
* *Beautiful Soup*: parse HTML
* *Webbrower/Selenium*: browser control
* *Scrapy*： https://docs.scrapy.org/en/latest/intro/tutorial.html

### 爬虫相关的参考资料

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter11/)
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/scenarios/scrape/)
* [Beginner’s guide to Web Scraping in Python (using BeautifulSoup)](https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/)

### Scraping example of IMDb Movie Ranking
IMDb is one of the largest movie databases in the world. It contains movie data and allows users to rate each movie.

It can also listed all the movies by year via: http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=2016,2017

By more 'digging', we can find that the next page of the above url can be retrieved by adding '&page=1&ref_=adv_nxt'

以下内容主要参考如下两个网站：

- https://www.dataquest.io/blog/web-scraping-beautifulsoup/
- https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-23.php



```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
```


```python
# 原始的URL拆分
oriurl = 'http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=2016,2017'
orisuf  = '&page=1&ref_=adv_nxt'
```


```python
# 设定初始和截止年份
starty = '2016'
endy = '2017'
num = 1
```


```python
movies_lst = []
#num = 1

# 原始URL的开头部分
url = 'http://www.imdb.com/search/title'
params = dict(sort='num_votes,desc', start=num, title_type='feature', 
                  year=starty + ',' + endy)
print(url)
print(params)
```


```python
# 用requests获得所提供URL的网页内容
r = requests.get(url, params=params)
print(r)
```


```python
# 用beautifulsoup将html的内容提取出来
bs = BeautifulSoup(r.text, 'html.parser')
print(bs)
```


```python
# 针对bs获得内容进行分析，按照网页规律提取出电影的各个元素
for movie in bs.findAll('div', {'class':'lister-item-content'}):
            title = movie.find('a').string
            year = movie.find('span', {'class':'lister-item-year text-muted unbold'}).string
            genres = movie.find('span', 'genre').string
            genres =  genres.strip('\n').strip()
            # 控制网页返回的错误，runtime是否为空，以免数据无法正常写入
            if movie.find('span', 'runtime') is not None:
                runtime = movie.find('span', 'runtime').string
            else:
                runtime = 0
            rating = movie.find('div', {'class':"inline-block ratings-imdb-rating"}).find('strong').string
            # 根据不同的情况确定电影的投票数和gross票房
            if len(movie.findAll('span', {'name':"nv"})) == 2:
                votes = movie.findAll('span', {'name':"nv"})[0].string
                gross = movie.findAll('span', {'name':"nv"})[1].string
            else:
                votes = movie.find('span', {'name':"nv"}).string
                gross = np.nan
            # 将所有信息存入一个列表
            movies_lst.append([title, year, genres, runtime, rating, votes, gross])   
```


```python
print(movies_lst[:5])
```


```python
# 将列表转为dataframe
movies = pd.DataFrame(movies_lst, columns=['title', 'year', 'genres', 'runtime', 'rating', 'votes', 'gross'])
print(movies.head())
```

### 数据抓取注意事项：

1. 不要一直持续不停的抓
    - Sleep
2. 代码反复使用
    - 考虑复用、通用性
    - Pay attention to code generalization
3. 数据清理必不可少
    - Even downloaded data from database, you will still need data cleaning.


### Data Cleaning

#### Text cleaning steps

**文本清理的常用步骤**

- 传统方式
    - 英文全变成小写（词性转换？），中文分词
    - 去掉标点、停用词？
- word2vec
    - 设置模型参数
    - 跑模型
- 常用exploration方法
    - 数词数
    - 出现次数最多的词


### List, tuple, dict, set


```python
# what will we get?
lst = [ 3, 1, 2*2, 1, 'hello', 10-1 ]
lst[4]
```




    'hello'




```python
lst.extend(['hello'])
```


```python
str2 = 'hello'
str[0] = 'Q'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-b95cc7781218> in <module>
          1 str2 = 'hello'
    ----> 2 str[0] = 'Q'
    

    TypeError: 'type' object does not support item assignment


# what will we get?

```
["four", "score", "and", "seven", "years"][2]
["four", "score", "and", "seven", "years"][0,2,3]
["four", "score", "and", "seven", "years"][[0,2,3]]
["four", "score", "and", "seven", "years"][[0,2,3][1]][1]
```


```python

```

List related methods:

 https://docs.python.org/3/tutorial/datastructures.html

### mutable and immutable variables

与其他编程语言类似，在Python中也有可改和不可改变量类型。

不可改类型：
- int, float, string
- tuple

可改类型：
- list, set
-大部分第三方包生成的数据类型


```python

```

## Tuple

tuple (元组)，可以看成是不可改的list


```python
test_tuple = (1.25, 'data')
```


```python

```

## set
set，可以看成是集合，里面包含不重复的，无序的一组objects


```python
test_set = set([1,2,3,4,3,2,1])
```


```python
test_set = {1,2,3,4,3,2,1}
```


```python
lst1 = [1,2,3,4]
lst2 = [4,3,2,1]


print(lst1 == lst2)

print(set(lst1) == set(lst2))
```


```python
t_set1 = set([1,2,3,4])
t_set2 = {3,4,5,6}

```

## dictionary
dictionary, dict, 字典，词典

无序序列，其中的元素为key:value的形式组成，也就是说不是单纯的一个个元素，而是每个元素都有一个key和一个value，成对组成。


```python
test_dict = {
    'name': 'Barack Obama',
'country': 'usa',
'profession': 'president',
'age': '53'
            }

```


```python
print(test_dict)
```

**练习**
- 获取一个dict里面的keys，values，items
- 遍历一个dict的keys，values及两者同时遍历


```python

```

**练习**

计算下面alphgo所包含的单词数，以及出现次数最多的10个单词，以及去掉常用“停用词”之后出现次数最多的10个单词


```python
alphgo = """
Deep Learning

AlphaGo relies on deep neural networks—networks of hardware and software that mimic the web of neurons in the human brain. With these neural nets, it can learn tasks by analyzing massive amounts of digital data. If you feed enough photos of cow in the neural net, it can learn to recognize a cow. And if you feed it enough Go moves from human players, it can learn the game of Go. But Hassabis and team have also used these techniques to teach AlphaGo how to manage time. And the machine certainly seemed to manage it better than the Korean grandmaster. Its clock still carried sixteen minutes.

The Google machine repeatedly made rather unorthodox moves that the commentators could quite understand. But that too is expected. After training on real human moves, AlphaGo continues its education by playing game after game after game against itself. It learns from a vast trove of moves that it generates on it own—not just from human moves. That means it is sometimes makes moves no human would. This is what allows it to beat a top human like Lee Sedol. But over the course of an individual game, it can also leave humans scratching their heads.

Then AlphaGo's clock ran out. Both players were down to 60 seconds for each move, and Lee Sedol had exceeded his 60 seconds twice. One more, and he would forfeit the game. Soon, the game crossed the four-and-a-half-hour mark, and it looked, for the first time in the match, like the two players would play the game out to the very end without either player resigning. It was that close.

Eyeing the board, Redmond started to count up the points that seemed available to each player, and it appeared that one had an edge. "Unfortunately for Lee Sedol," he said, "I think white might have a slight advantage here." And as the game stretched to five hours, Redmond began to concede victory to AlphaGo. But it was hard to tell, he said, where Lee Sedol had gone wrong. Seconds later, the Korean resigned.

The game showed that AlphaGo is far from infallible. Early in the contest, it made a mistake that even a decent human player would not make. There are holes in its education. But, able to draw on months of play with itself—on a corpus of moves that no human has even seen—it also has the ability to climb out of such a deep hole, even against one of the world's best players. AI is flawed. But it is here.
"""
```


```python

```
