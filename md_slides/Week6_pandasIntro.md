# Python For Data Analysis
## Lecture 6 Data Cleaning & Pandas Intro

This lecture will talk about the basic steps of data cleaning and some methods of pandas packages.

The aim of the basic methods is to get(via index/slicing), modify, and remove data(including indexes) of a dataframe(series)

## Data Cleaning

数据清理其实从数据抓取的时候就开始。

请思考，你抓取/获得的数据是以什么格式存储的？

- 是以什么格式存储的？
- 是否分栏？
- 每栏的内容是什么？
- 每行的内容是什么？

同样的数据内容，可以以不同的文件类型、数据格式，数据内容…保存

### 数据清理及探索在数据导入python前后的主要内容

1. 获取数据之后，读入Python之前：
    * 目的：了解数据
    * 确保读入的数据的方式以及读入的数据与原始数据相同,以免程序出错
    * 在此阶段只能探索全部数据的“部分”信息
2. 读入Python之后
    * 目的：将数据转换为满足跑模型数据
    * 包含但不限于，量化、整合、归一等

3. 数据探索将全面围绕在数据清理的各个方面
    * “重复”探索

### [读入Python前的数据探索](#dtexp-bf-read)

1. 打开文件之前：
    - 数据是以哪种“文件”存储的？
    - 是哪种文件类型？文本？图片？

2. 打开文件之后：
    - 观察文档的“结构”
    - 是否分行？多少行？
    - 是否分栏？多少栏？
3. 思考
    - 适合用哪种Python方法读入数据？
    - 文件所处位置与代码文件位置？
    - 文档编码？

## Pandas

Pandas是数据分析和科学领域最常用的包，以table表格为主要数据类型

* 官方文档： https://pandas.pydata.org/docs/user_guide/index.html#user-guide

* 非官方中文文档：
  https://www.pypandas.cn/docs/user_guide/

Pandas两种主要的数据类型：
- series：Numpy array + index组成的字典
- dataframe：series 组成的字典


```python
# Check your pandas version
import pandas as pd
import numpy as np
print(pd.__version__)
print(np.__version__)
```


```python
dates = pd.date_range('20130101', periods=6)
print(dates)
# create a dataframe with dates as index and column names as "ABCD" with random values
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
```


```python
print(df['A'])
print(type(df['A']))
```


```python
print(df.A.values)
print(type(df.A.values))
```


```python
# python list
test_lst = list(range(10,20))
print(test_lst)
```


```python
# Numpy array
test_ary = np.array(test_lst)
test_ary
```

### Series



```python
# 一组带index的array
test_srs = pd.Series(test_lst)
test_srs
```


```python
print(test_srs.values)
print(test_srs.index)
```


```python
# create a series with assigned index
test_srs2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['A','B','C','D'])
print(test_srs2)
```

Series的value的数据类型是什么？


```python

```

## Numpy

官方教程：https://numpy.org/doc/stable/user/quickstart.html


Numerical Python的简称,高性能科学计算和数据分析的基础包(T4, ch2).
Provides the most important data types for econometrics, statistics and numerical analysis.
主要的数据类型是ndarry(数组)和 matrix(矩阵)

### Array
Arrays can have 1,2,3 or more dimensions, which are commonly used in scientific computing.

- Numpy的“list”
    - list每个元素可以是不同的数据类型，array只能是单一类型
    - array可以进行更多的数学方面的操作
- Array/metrix 拥有不同的数学操作


```python
tt_lst = [1, 2.5,'hello']
print(tt_lst)
arr1 = np.array(tt_lst)
print(tt_lst)
```


```python
arr1.dtype
```


```python
tt_lst = list(range(10000))
arr1 = np.array(tt_lst)
```


```python
# timeit
[i**2 for i in tt_lst]
```


```python
arr1**2
```

#### index/slice

Array 的index， slice方法与list类似

#### Array ufunc
- 教材
    - T4，ch2.3
- 官方英文介绍：
    - https://numpy.org/doc/stable/reference/ufuncs.html
- 非官方中文介绍：
    - https://www.pythonf.cn/read/102939


## Pandas

* 最常用的一个数据处理包
* 表格式数据结构
* 集成时间序列和非时间序列
* 合并其他常见的数据库，包括sql的关系型运算

### Read file to pandas

- pandas提供多种文件格式的读入
    - 取决于自己文件（硬盘上）的文件类型
    - DO NOT “trust” the file extension
- 在用python读取之前，一定先完成之前的[探索步骤](UG_Lecture_8.ipynb#dtexp-bf-read)
    - Understand the file format/structure


**善用TAB键获得相关代码提示**

pd.read_<tab>

### 数据读入之后的操作

1. 读入数据
2. 核对读入数据完整性
   - 核对栏名、行名
   - 栏数、行数
   - 第一行、最后一行等
3. 对数据进行初步探索
   - 各栏的数据类型


### 一个好玩的自学机会

打开下面两个网页的任意一个，然后倒计时10分钟。看看阅读之后能“理解”多少 :)

- 官方英文版：
    - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
- 非官方中文版
    - https://www.pypandas.cn/docs/getting_started/10min.html#%E5%8D%81%E5%88%86%E9%92%9F%E5%85%A5%E9%97%A8-pandas 


#### 根据上面的文档，判断读入的文件是否完整，有缺漏：

1. print出栏名、行名
2. 判断一共多少栏、多少行
3. print出前8行、最后10行等


```python
dates = pd.date_range('20130101', periods=6)
print(dates)
# create a dataframe with dates as index and column names as "ABCD" with random values
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
```


```python

```

### dataframe

类似于由series组成的字典(dict)

- 对行、列的操作完全相同
- 对行、列可以进行整体操作
- 基于行列的整体运算速度非常快
    - 在pandas中尽量少用for循环


#### index/slice

dataframe的index和取值主要有以下几个方式：

1. df[栏名]，df.栏名：获取一栏的全部内容（如何获得多栏？）
2. df.loc：根据label取值
3. df.iloc:根据index取值


```python

```

#### 练习
- 分别用 df[], df.loc, df.iloc 获取所有电影的ratings一栏
- 得到ratings高于8.6的所有电影
- 得到‘Forrest Gump’这部电影的全部信息
- 选择2010年以来，ratings为8.8以上的电影，并按照ratings的大小排序（分值高在上）
    - Sort_values


### Pandas Basic Methods

How to get the index and column names of a dataframe or a series?

How to modeify/remove the index and column name(s)?

**Exercise**
- Set 'A' as the index of uni
- Rename the column 'C' to 'CC'


```python

```


```python

```

**Exercies**
- Delete the 'D' column
- Assign the value of the first three columns to a new variable.


```python

```

### inplace
Have you noticed that most of the above mehods did not 'actually' changed the dataframe? Why?

Most of Pandas methods have a argunment 'inplace', which indicates whether to revised the original dataframe or return a new one.

## Data Cleaning
### The basic workflow for the early stages of exploratory data
* Build ​the DataFrame. It should have the following properties:
    * Deal with missing data
    * Each row describes a single object
    * Each column describes a property of that object
    * Columns are numeric whenever appropriate
    * Columns contain atomic properties that cannot be further decomposed
* Explore global properties. 
    * Use histograms, scatter plots, and aggregation functions to summarize the data.
* Explore group properties. 
    * Use groupby and small multiples to compare subsets of the data.


```python

```
