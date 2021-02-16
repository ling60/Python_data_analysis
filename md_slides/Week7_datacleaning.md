# Python for Data Science
## Week 9
This lecture will introduce the cleaning process of iMDB data


```python
# 以下设置的目的是为了让让pandas在notebook中有更好的显示效果

import pandas as pd
# change pandas default settings to show more rows and columns of data
# more information please refer to : https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 10)
# surpass the scientific notation
pd.set_option('display.float_format', lambda x: '%.3f' % x)
```

## 数字数据的清理

虽然我们的信息源很多，信息原始格式也不尽相同，但无论本身就是数字类型的数据，还是文本、视频、图片等其他类型的数据，在带入模型之前，我们终将用数字来表示。

比如，我们会用向量的形式代表图片，用定类的数字代表“男女”这样的类不选项（这部分请参见第三个课程内容）。因此，对数字类数据的清理尤为重要。

本次课将以pandas为主来介绍在社科领域常见的数字类数据的清理问题。

### 数据清理的主要步骤


- 尽量将所有数据合并在一个变量(dataframe)内
- 对数据进行探索
    - 全局探索
    - 分组探索
- 数据清理
    - 处理缺失值
    - 行代表样本，列代表样本的各个属性
    - 保证每一个属性的值都是单一的
    - 尽量将所有的数据都变为数字类型



```python

```

### Data Cleaning

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
# 读取文件
imdb = pd.read_table('data/imdb_10000_1990_2020.txt')
```


```python
imdb.head()
```

#### 数据初步探索

了解自己的数据是非常非常非常重要的。以下步骤需要在数据分析的全过程中反复查验

- 验证数据完整性
	- 读入或运行程序后是否产生查错
	- 数据行数、列数
	- 数据量
- 了解数据
	- 每列数据的类型
	- 各个属性的最大、最小、均值（mean, median）等
	- 异常值


**练习**

对imdb数据进行初步探索，并分析当前的问题

```
df.info()
df.describe()
```


```python
imdb.info()
```

### 数据缺失missing data

* Pandas默认把缺失数据列为,NaN
* missing (缺失)也指 null 或者 ‘not present for whatever reason’
* 有些数据集就没有搜集到相应的数据,或者数据本身存在,但没有搜集到,等等比如同一时间段不同股票的股价有的可能会有缺失
* 在数据转换过程中也可能出现数据缺失,比如,将正常股价数据集添加上周末日期

```
df.isnull()
pd.isnull(df)
df.notnull()
df.ffill()
df.fillna(0)  # 用’missing’来代替NaN
```

**练习** 找到IMDb中的缺失值


```python
imdb.info()
```

**练习**
找到imdb中的缺失值，考虑如何对其进行处理？
* 删除
* 用其他值填充
* 找到相关数据再填充


```python
imdb.isnull().any()
```

### Clean Data
按照上面的方法分析需要做哪些清理，并完成基本的数据清理


```python
imdb.head()
```

#### 以runtime为例

1. 判断值的共性
2. 以一个cell里面的值为例进行尝试
3. 将方法应用到全部行

当前runtime一栏数据类型是字符串，我们需要将runtime最后的“ min”去掉，并将里面的数据转换为数字类型（int/float）.


```python
# 判断某一部电影的runtime是否以min结束
imdb.iloc[2,3].endswith('min')
```


```python
# 判断是否runtime这一列最后都是以min结束
imdb.loc[~imdb.runtime.str.endswith('min')]
```


```python
# 针对某一部电影的runtime 进行修正
float(imdb.iloc[2,3][:-4])
```


```python
# 应用到全部行
rtlst = []
for rt in imdb.runtime:
    rtlst.append(int(rt[:-4]))
```


```python
# 检查数据正确性，赋值/应用
```


```python
%timeit [int(rt[:-4]) for rt in imdb.runtime]
```


```python
%timeit imdb.runtime.apply(lambda x:int(x[:-4]))
```


```python
# 再次探查数据，检查结果
imdb.runtime = [float(rt[:-4]) for rt in imdb.runtime]
```


```python
imdb.describe()
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
      <th>runtime</th>
      <th>rating</th>
      <th>metascore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000</td>
      <td>10000.000</td>
      <td>7173.000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>108.659</td>
      <td>6.420</td>
      <td>55.488</td>
    </tr>
    <tr>
      <th>std</th>
      <td>21.056</td>
      <td>1.026</td>
      <td>17.568</td>
    </tr>
    <tr>
      <th>min</th>
      <td>43.000</td>
      <td>1.000</td>
      <td>1.000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>94.000</td>
      <td>5.800</td>
      <td>43.000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>104.000</td>
      <td>6.500</td>
      <td>56.000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>118.000</td>
      <td>7.100</td>
      <td>68.000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>439.000</td>
      <td>9.300</td>
      <td>100.000</td>
    </tr>
  </tbody>
</table>
</div>




```python
imdb.loc[imdb.runtime>200]
```


```python
# 依次完成剩下几栏的清理
for g in imdb.gross:
    try:
        g[1:-1]
    except:
        continue
```


```python

```


```python
imdb.runtime.apply(lambda y: int(y[:-4]))

imdbtitle = imdb.title + imdb.year.str[:-6]

imdbyear = imdb.year.str[-5:-1].astype(int)

imdb.title = imdbtitle.str.strip()

imdb.year = imdbyear

imdb.votes = imdb.votes.str.replace(',', '').astype(int)

imdb.gross = pd.to_numeric(imdb.gross.str[1:-1])
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Shawshank Redemption</td>
      <td>1994</td>
      <td>Drama</td>
      <td>142 min</td>
      <td>9.300</td>
      <td>80.000</td>
      <td>2295181</td>
      <td>28.340</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Dark Knight</td>
      <td>2008</td>
      <td>Action, Crime, Drama</td>
      <td>152 min</td>
      <td>9.000</td>
      <td>84.000</td>
      <td>2259996</td>
      <td>534.860</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Inception</td>
      <td>2010</td>
      <td>Action, Adventure, Sci-Fi</td>
      <td>148 min</td>
      <td>8.800</td>
      <td>74.000</td>
      <td>2022025</td>
      <td>292.580</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fight Club</td>
      <td>1999</td>
      <td>Drama</td>
      <td>139 min</td>
      <td>8.800</td>
      <td>66.000</td>
      <td>1819764</td>
      <td>37.030</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pulp Fiction</td>
      <td>1994</td>
      <td>Crime, Drama</td>
      <td>154 min</td>
      <td>8.900</td>
      <td>94.000</td>
      <td>1792404</td>
      <td>107.930</td>
    </tr>
  </tbody>
</table>
</div>




```python
imdb.describe()
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
      <th>year</th>
      <th>rating</th>
      <th>metascore</th>
      <th>votes</th>
      <th>gross</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000</td>
      <td>10000.000</td>
      <td>7173.000</td>
      <td>10000.000</td>
      <td>7105.000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2007.515</td>
      <td>6.420</td>
      <td>55.488</td>
      <td>65510.689</td>
      <td>34.924</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.018</td>
      <td>1.026</td>
      <td>17.568</td>
      <td>135975.714</td>
      <td>64.157</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1990.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>4668.000</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2002.000</td>
      <td>5.800</td>
      <td>43.000</td>
      <td>8337.750</td>
      <td>0.880</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2009.000</td>
      <td>6.500</td>
      <td>56.000</td>
      <td>18724.000</td>
      <td>11.110</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2014.000</td>
      <td>7.100</td>
      <td>68.000</td>
      <td>60027.000</td>
      <td>40.980</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2020.000</td>
      <td>9.300</td>
      <td>100.000</td>
      <td>2295181.000</td>
      <td>936.660</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 手工添加所有电影类型
gens_set = set()
for g in imdb.genres:
    gens.update(g.split(','))
# 去掉不同的空格
gens_set = {i.strip() for i in gens}
print(gens_set)
```

    {'Action', 'Music', 'Mystery', 'Sci-Fi', 'Drama', 'Crime', 'Comedy', 'Thriller', 'Romance', 'Biography', 'Animation', 'Western', 'Sport', 'Musical', 'History', 'War', 'Horror', 'Adventure', 'Fantasy', 'Family'}
    


```python
# 遍历gens_set这个所有电影类型的set中的各个电影类型（gen）
for gen in gens_set:
    # 生成一个针对所有电影对应该类型gen的1/0的列表
    movies_gens = []
    # 遍历dataframe里面各部电影的电影类型一栏，即，imdb.genres
    for movie_gen in imdb.genres:
        # 判断当前遍历的电影类型（gen）是否出现在该电影对应的电影类型（movie_gen）里
        # 因为genres字符串中，有的电影类型前面有空格，所以需要用strip把空格去掉
        if gen in [i.strip() for i in movie_gen.split(',')]:
            
            movies_gens.append(1)
        else:
            movies_gens.append(0)
    imdb[gen] = movies_gens  
```


```python
# 如果不用strip可以采用split加入参数"(', '')"

# 以Dark Knight为例，其电影类型为：
print(imdb.iloc[1,2])
# 直接以逗号split，可以看到有空格
print(imdb.iloc[1,2].split(','))
# 以逗号+空格split，可以看到没有空格了
print(imdb.iloc[1,2].split(', '))
```

    Action, Crime, Drama
    ['Action', ' Crime', ' Drama']
    ['Action', 'Crime', 'Drama']
    


```python
imdb.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10000 entries, 0 to 9999
    Data columns (total 28 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   title      10000 non-null  object 
     1   year       10000 non-null  int32  
     2   genres     10000 non-null  object 
     3   runtime    10000 non-null  object 
     4   rating     10000 non-null  float64
     5   metascore  7173 non-null   float64
     6   votes      10000 non-null  int32  
     7   gross      7105 non-null   float64
     8   Action     10000 non-null  int64  
     9   Music      10000 non-null  int64  
     10  Mystery    10000 non-null  int64  
     11  Sci-Fi     10000 non-null  int64  
     12  Drama      10000 non-null  int64  
     13  Crime      10000 non-null  int64  
     14  Comedy     10000 non-null  int64  
     15  Thriller   10000 non-null  int64  
     16  Romance    10000 non-null  int64  
     17  Biography  10000 non-null  int64  
     18  Animation  10000 non-null  int64  
     19  Western    10000 non-null  int64  
     20  Sport      10000 non-null  int64  
     21  Musical    10000 non-null  int64  
     22  History    10000 non-null  int64  
     23  War        10000 non-null  int64  
     24  Horror     10000 non-null  int64  
     25  Adventure  10000 non-null  int64  
     26  Fantasy    10000 non-null  int64  
     27  Family     10000 non-null  int64  
    dtypes: float64(3), int32(2), int64(20), object(3)
    memory usage: 2.1+ MB
    


```python
imdb.describe()
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
      <th>year</th>
      <th>rating</th>
      <th>metascore</th>
      <th>votes</th>
      <th>gross</th>
      <th>...</th>
      <th>War</th>
      <th>Horror</th>
      <th>Adventure</th>
      <th>Fantasy</th>
      <th>Family</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000</td>
      <td>10000.000</td>
      <td>7173.000</td>
      <td>10000.000</td>
      <td>7105.000</td>
      <td>...</td>
      <td>10000.000</td>
      <td>10000.000</td>
      <td>10000.000</td>
      <td>10000.000</td>
      <td>10000.000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2007.515</td>
      <td>6.420</td>
      <td>55.488</td>
      <td>65510.689</td>
      <td>34.924</td>
      <td>...</td>
      <td>0.584</td>
      <td>0.584</td>
      <td>0.584</td>
      <td>0.584</td>
      <td>0.584</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.018</td>
      <td>1.026</td>
      <td>17.568</td>
      <td>135975.714</td>
      <td>64.157</td>
      <td>...</td>
      <td>0.493</td>
      <td>0.493</td>
      <td>0.493</td>
      <td>0.493</td>
      <td>0.493</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1990.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>4668.000</td>
      <td>0.000</td>
      <td>...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2002.000</td>
      <td>5.800</td>
      <td>43.000</td>
      <td>8337.750</td>
      <td>0.880</td>
      <td>...</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2009.000</td>
      <td>6.500</td>
      <td>56.000</td>
      <td>18724.000</td>
      <td>11.110</td>
      <td>...</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2014.000</td>
      <td>7.100</td>
      <td>68.000</td>
      <td>60027.000</td>
      <td>40.980</td>
      <td>...</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2020.000</td>
      <td>9.300</td>
      <td>100.000</td>
      <td>2295181.000</td>
      <td>936.660</td>
      <td>...</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
      <td>1.000</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 25 columns</p>
</div>




```python

```


```python
# 综合上面的方法，我们可以将代码简化为如下一行
for gen in gens_set:
    imdb[gen] = [1 if gen in i.split(', ') else 0 for movie_gen in imdb.genres]
```


```python
# 然而还有更简便的方法
imdb.genres.str.get_dummies(sep=', ')
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
      <th>Action</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>...</th>
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
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>10000 rows × 20 columns</p>
</div>




```python

```
