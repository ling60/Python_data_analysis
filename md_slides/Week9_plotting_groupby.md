# Python for Data Analysis
## Week 11
In this lecture, we will keep analyzing IMDb data. We will have a look at the data's global and group exploration.

In the meantime, we will introduce data plotting in Python and Pandas.

### The basic workflow for the early stages of exploratory data
* Build a DataFrame from the data (ideally, put all data in this object)
* Clean the DataFrame. It should have the following properties:
    * Deal with missing data
    * Each row describes a single object
    * Each column describes a property of that object
    * Columns are numeric whenever appropriate
    * Columns contain atomic properties that cannot be further decomposed
* Explore global properties. 
    * Use histograms, scatter plots, and aggregation functions to summarize the data.
* Explore group properties. 
    * Use groupby and small multiples to compare subsets of the data.


```python
import pandas as pd
# change pandas default settings to show more rows and columns of data
# more information please refer to : https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 30)
# surpass the scientific notation
pd.set_option('display.float_format', lambda x: '%.3f' % x)
```


```python
import matplotlib.pyplot as plt
# 下面一行语句的意思是为了让matplotlib可以在notebook里面直接显示图
%matplotlib inline
```

## matlab.pyplot

有两种接口：


- pyplot接口

便捷接口，直接使用plt.plot()画图，较为简单，且pandas嵌入的画图方式多为这类接口。但对多图及个性化设置稍为复杂

```
plt.plot()
```
- 面对对象接口

功能更为强大，需要生成figure, ax两个对象，学习成本较高，但是可定制化更强

```
fig = plt.subplot()
ax = plt.subplot()
ax.plot()
```

plt.plot()和ax.plot()两种接口的参数基本一致，只有稍许不同


```python
# creat sample data

import numpy as np
x = np.linspace(0,10,100)
print(x)
```

    [ 0.          0.1010101   0.2020202   0.3030303   0.4040404   0.50505051
      0.60606061  0.70707071  0.80808081  0.90909091  1.01010101  1.11111111
      1.21212121  1.31313131  1.41414141  1.51515152  1.61616162  1.71717172
      1.81818182  1.91919192  2.02020202  2.12121212  2.22222222  2.32323232
      2.42424242  2.52525253  2.62626263  2.72727273  2.82828283  2.92929293
      3.03030303  3.13131313  3.23232323  3.33333333  3.43434343  3.53535354
      3.63636364  3.73737374  3.83838384  3.93939394  4.04040404  4.14141414
      4.24242424  4.34343434  4.44444444  4.54545455  4.64646465  4.74747475
      4.84848485  4.94949495  5.05050505  5.15151515  5.25252525  5.35353535
      5.45454545  5.55555556  5.65656566  5.75757576  5.85858586  5.95959596
      6.06060606  6.16161616  6.26262626  6.36363636  6.46464646  6.56565657
      6.66666667  6.76767677  6.86868687  6.96969697  7.07070707  7.17171717
      7.27272727  7.37373737  7.47474747  7.57575758  7.67676768  7.77777778
      7.87878788  7.97979798  8.08080808  8.18181818  8.28282828  8.38383838
      8.48484848  8.58585859  8.68686869  8.78787879  8.88888889  8.98989899
      9.09090909  9.19191919  9.29292929  9.39393939  9.49494949  9.5959596
      9.6969697   9.7979798   9.8989899  10.        ]
    


```python
# plt.plot()接口
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
```


```python
help(plt.plot)
```

### plt.plot() 参数

详细信息见：

https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

最重要的三个参数：

- x,y: 坐标轴x，y轴的数据。两组数据时，第一组是x第二组是y。一组数据默认为y，x则自动生成range（0,n）,n为y数据的个数
- fmt: formatstring，这个参数表示画出图形的格式，参数类型为字符串，具体对应如下：

    fmt = '[marker][line][color]' 意思是，参数最多由三部分组成，第一部分代表每个数据点对应的标识，第二部分代表是线还是点，第三部分代表颜色。每个部分都是可选的

- data: 当数据为object，比如dataframe的时候，我们可以把df变量传递给data这个参数部分，而后在x,y的地方直接传递对应的栏名



```python

plt.plot(x, np.sin(x),',')
```


```python
imdb_clean = pd.read_csv('data/imdb_clean.csv')
imdb_clean.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>genres</th>
      <th>runtime</th>
      <th>rating</th>
      <th>metascore</th>
      <th>votes</th>
      <th>gross</th>
      <th>Action</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>Crime</th>
      <th>Drama</th>
      <th>Family</th>
      <th>Fantasy</th>
      <th>History</th>
      <th>Horror</th>
      <th>Music</th>
      <th>Musical</th>
      <th>Mystery</th>
      <th>Romance</th>
      <th>Sci-Fi</th>
      <th>Sport</th>
      <th>Thriller</th>
      <th>War</th>
      <th>Western</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Shawshank Redemption</td>
      <td>1994</td>
      <td>Drama</td>
      <td>142</td>
      <td>9.300</td>
      <td>80.000</td>
      <td>2295181</td>
      <td>28.340</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Dark Knight</td>
      <td>2008</td>
      <td>Action, Crime, Drama</td>
      <td>152</td>
      <td>9.000</td>
      <td>84.000</td>
      <td>2259996</td>
      <td>534.860</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Inception</td>
      <td>2010</td>
      <td>Action, Adventure, Sci-Fi</td>
      <td>148</td>
      <td>8.800</td>
      <td>74.000</td>
      <td>2022025</td>
      <td>292.580</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fight Club</td>
      <td>1999</td>
      <td>Drama</td>
      <td>139</td>
      <td>8.800</td>
      <td>66.000</td>
      <td>1819764</td>
      <td>37.030</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pulp Fiction</td>
      <td>1994</td>
      <td>Crime, Drama</td>
      <td>154</td>
      <td>8.900</td>
      <td>94.000</td>
      <td>1792404</td>
      <td>107.930</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
imdb = imdb_clean.sort_values('year')
```


```python
imdb.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>genres</th>
      <th>runtime</th>
      <th>rating</th>
      <th>metascore</th>
      <th>votes</th>
      <th>gross</th>
      <th>Action</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>Crime</th>
      <th>Drama</th>
      <th>Family</th>
      <th>Fantasy</th>
      <th>History</th>
      <th>Horror</th>
      <th>Music</th>
      <th>Musical</th>
      <th>Mystery</th>
      <th>Romance</th>
      <th>Sci-Fi</th>
      <th>Sport</th>
      <th>Thriller</th>
      <th>War</th>
      <th>Western</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8017</th>
      <td>Ghost Dad</td>
      <td>1990</td>
      <td>Comedy, Family, Fantasy</td>
      <td>83</td>
      <td>4.400</td>
      <td>nan</td>
      <td>7370</td>
      <td>24.710</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4550</th>
      <td>Cyrano de Bergerac</td>
      <td>1990</td>
      <td>Comedy, Drama, History</td>
      <td>137</td>
      <td>7.500</td>
      <td>79.000</td>
      <td>22201</td>
      <td>15.140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6934</th>
      <td>Dip huet gai tau</td>
      <td>1990</td>
      <td>Action, Crime, Drama</td>
      <td>136</td>
      <td>7.600</td>
      <td>nan</td>
      <td>9723</td>
      <td>nan</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1910</th>
      <td>Teenage Mutant Ninja Turtles</td>
      <td>1990</td>
      <td>Action, Adventure, Comedy</td>
      <td>93</td>
      <td>6.800</td>
      <td>51.000</td>
      <td>84251</td>
      <td>135.270</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8451</th>
      <td>Class of 1999</td>
      <td>1990</td>
      <td>Action, Horror, Sci-Fi</td>
      <td>99</td>
      <td>5.900</td>
      <td>33.000</td>
      <td>6614</td>
      <td>2.460</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
imdb.groupby('year').runtime.rolling(3).mean()
```




    year      
    1990  8017       nan
          4550       nan
          6934   118.667
          1910   122.000
          8451   109.333
                   ...  
    2020  5617   108.333
          7113    98.667
          7435   104.333
          2329   113.667
          8027   109.667
    Name: runtime, Length: 10000, dtype: float64




```python
imdb.groupby('year').runtime.apply(lambda x: x[2:]).mean()
```




    108.67156369490843




```python

```


```python
plt.plot('rating','.', data=imdb_clean)
```

### 面对对象的接口

主要目的是创建两个实例(instance)

- figure,代表画布
- axes，代表坐标轴

画图的时候需要使用：
```
ax.plot()
```
里面参数与plt.plot()基本一致。但在axes里面可以对坐标轴做更多的设置和个性化处理。具体见：

https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes


除此之外，我们还需要了解图形中各个不同部位的名称，具体如下图所示：
    
[matplotlib中图形对应的名称](https://matplotlib.org/3.3.3/_images/anatomy.png)


```python
# 面对对象接口
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x))
# ax.plot(np.cos(x))
```


```python
plt.style.use('seaborn-paper')

```


```python
plt.style.available
```

### 线图之外

plt.plot()主要是画线图，除此之外，plt还提供了其他图形，具体可见：
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html

常见的如下：

- scatter, 散点图
- hist，频次直方图



```python
imdb_clean.corr()
```


```python

```

### Pandas plotting

pandas 基本上移植/嵌入了plt里绝大部分的图形，具体见：
https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html


除直接调用对应的图形function之外，还可以在plot里面用kind=这个参数做控制:

kind=

- ‘bar’ or ‘barh’ for bar plots
- ‘hist’ for histogram
- ‘box’ for boxplot
- ‘kde’ or ‘density’ for density plots
- ‘area’ for area plots
- ‘scatter’ for scatter plots
- ‘hexbin’ for hexagonal bin plots
- ‘pie’ for pie plots


```python
# imdb_clean.hist('rating')
# 需将对应的属性传递给y参数
imdb_clean.plot(y='rating', kind='hist')
```


```python
imdb_clean.rating.plot(kind='kde')
```


```python
imdb_clean.columns
```


```python
imdb_clean.plot( 'rating', 'votes',kind='scatter')
```


```python
imdb_clean.describe()
```

### Exploration

#### What to know?

1. Variable identification
    - define the type of every variable
2. Data Exploration
    - missing value
    - max/min
    - data distribution/Central tendencies
    - outlier
    - duplicates
3. Bi-Variable analysis
    - Continuous & Continuous: We can build a scatter plots in order to see how two continuous variables interact between each other.
    - Categorical & Categorical: A Stacked Column Chart is a good visualization that shows how the frequencies are spread between the two categorical variables.
    - Categorical & Continuous: boxplots combined with swarmplots.


```python
action = imdb_clean[(imdb_clean.year>2014) & (imdb_clean.Action == 1) & (imdb_clean.metascore.notnull())]
```


```python
imdb_clean[imdb_clean.duplicated('title', keep=False)].sort_values('title')
```


```python
imdb_clean.rank?
```


```python
imdb_clean.duplicated?
```

## Global Properties Exploration
- 查看分数最高、最低的影片
- 查看各个类型电影的数量，评分
- 找出数据中的outlier

- 画图显示各年电影数量
- 画图展示所有电影评分的分布情况


```python
imdb_clean.groupby("year").size().plot(kind='bar')
```


```python
imdb_clean[imdb_clean.year==1991]
```

### Groupby
分组, pandas非常强大的一个地方

将dataframe中的数据,以某一栏内的值来分组(性别,专业等),然后进行相关运算

阅读Pands文档,groupby相关内容

```
gb = df_u.groupby(‘qsstars’)
gb.mean()
gb.max()
gb.size()
```


```python
gp = imdb_clean.groupby('year')
```


```python
gp.mean()
```


```python
genres = ['Adventure', 'Fantasy', 'Music', 'War', 'Mystery', 'Comedy', 'Action', 'History', 'Family', 'Sport', 'Horror', 'Drama', 'Thriller', 'Crime', 'Musical', 'Western', 'Biography', 'Animation', 'Romance', 'Sci-Fi']
```


```python
gendf = pd.Series()
for g in genres:
    gendf[g] = len(imdb_clean[imdb_clean[g]==1])
```


```python
gendf.hist()
```


```python

```


```python
imdb_clean.groupby('year')['rating'].median().plot()
```


```python

```

## Group property exploration
**练习**
* 每个时代（decade，十年）汇总相关信息
* 创建decade一栏，标记出每个电影所在的decade


```python
imdb_clean['five_year'] = 
```


```python
imdb_clean.groupby('year').rating.mean()
```


```python
imdb_clean.columns
```


```python
imdb_clean.genres.str.split(', ').str.len().max()
```


```python

```
