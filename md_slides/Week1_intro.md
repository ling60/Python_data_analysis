# 数据分析編程（Python）

本课程是西南财经大大学开设的一门公选课，课程主要内容为介绍如何利用Python语言在数据分析的过程中进行更简便、快捷的操作。

全课程预计为15-17周，中间包括一次限时作业和一次总结。

本篇为第一周的课程，主要内容为介绍数据科学、Python语言。

## 数据科学(Data Science)介绍

### 定义

> Definition: A central challenge of data science is to make reliable conclusions using partial information。

数据科学经过长时间的发展，目前已经变为一门涉猎颇广的学科，很多国内外高校都已经开始开设数据科学专业。

数据科学的基本含义是通过一系列科学的方法，利用部分数据对事务做出可靠的判断。

### 目标

当下数据科学有三个主要方向，或者说，我们分析数据最后的目的有三个：

1. Expolartion, 对数据进行探索
2. Predication/Inference, 预测/统计推断
3. Cause Effect Analysis， 因果分析

**Exploration**

对数据进行探索的意思可以看成对“了解情况”的过程。即，通过搜集大规模的数据，了解当下正在发生的事情。比如，目前男女比例多少，本科生毕业就业率如何等等。复杂一些的还有，某个游戏的用户画像，比如，王者荣耀的用户年龄、兴趣、学历、性别分布等等。

**Prediction/Inference**

预测和推断其实是相似的内容，都是意图根据已有的数据推测其他的未知的数据结果。比如，明天股价如何？严格考勤制度是否能够提供学生的学习成绩？但，在数据科学里，我们通常把利用机器学习方法得到的很多结果叫做预测，而通过统计或计量模型得到的结果则称之为推断

**Causal Effect**

因果分析是数据分析中非常重要也是较为困难的一个方向，因为我们需要确定两个变量之间到底是否存在因为A导致B的结果。比如，上面举过的一个例子，严格考勤制度是否能够提供学生的学习成绩？这个问题本身是个推断类的问题，但是，如果我们进一步继续验证，想知道，学生出勤率是否会影响他的成绩？那么就变成了一个因果分析的过程。

### 数据分析的流程

数据分析是一个广泛应用在各个领域的一个方法（学科），但总体而言，都可以分为一下几个步骤：

1. 数据获取
2. 数据清理
3. 数据建模
4. 结果展示

在整个分析的过程中，我们会遇到很多繁琐、重复的活动，因此，如果能有一个工具可以贯穿分析的始终，并且在每个步骤中都能起到很好的效果，将会大大提高我们的效率。

Python就是一门非常适合用来做数据分析的编程语言。

## Introduction to Python

### Why Python？

Python的特点是语法及其简单，跟普通英语相似。更为重要的是，Python目前有着非常良好蓬勃发展的“社区”。很多学者、公司、程序员都提供了大量可以重用的代码包，因此就不必“重新制造轮子”，我们只要了解这些包（package）的具体用法就可以了。

###  安装及IDE

如果想利用Python做数据分析，或者学完整个课程，我们强烈建议直接安装[Anaconda](https://www.anaconda.com/products/individual). 这是一个包含了上千个Python常用库的集合，使用起来非常方便。

具体安装方法见：

[Anaconda的安装方法 ](../Anaconda_installsetup.md)

常用的IDE有：
1. IPython + Text editor(notepad++, vim, etc)
2. Spyder, 安装anaconda后，自带，无需额外安装
3. [Jupyter Noteboo] (https://zhuanlan.zhihu.com/p/242524977）)
4. Pycharm。社区版免费

## Python的数据类型
- string，字符串
- numerical, 数字类，int,float
- list，列表
- dict，字典
- tuple，元组
- set，集合