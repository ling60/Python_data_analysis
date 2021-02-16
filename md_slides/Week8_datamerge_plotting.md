# Python for Data Analysis

## Week 8: data cleaning and plotting

In this lecture, we will summarize on the cleaness of IMDb data. Then we will introduce data visualization and data merge in Python and Pandas.


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

import numpy as np
import random
```

### imdb数据清理


```python
imdb = pd.read_table('data/imdb_10000_1990_2020.txt')

print(imdb.head())
```

                          title    year                     genres  runtime  rating  metascore      votes     gross
    0  The Shawshank Redemption  (1994)                      Drama  142 min   9.300     80.000  2,295,181   $28.34M
    1           The Dark Knight  (2008)       Action, Crime, Drama  152 min   9.000     84.000  2,259,996  $534.86M
    2                 Inception  (2010)  Action, Adventure, Sci-Fi  148 min   8.800     74.000  2,022,025  $292.58M
    3                Fight Club  (1999)                      Drama  139 min   8.800     66.000  1,819,764   $37.03M
    4              Pulp Fiction  (1994)               Crime, Drama  154 min   8.900     94.000  1,792,404  $107.93M



```python
imdb.runtime.apply(lambda y: int(y[:-4]))

imdbtitle = imdb.title + imdb.year.str[:-6]

imdbyear = imdb.year.str[-5:-1].astype(int)

imdb.title = imdbtitle.str.strip()

imdb.year = imdbyear

imdb.votes = imdb.votes.str.replace(',', '').astype(int)

imdb.gross = pd.to_numeric(imdb.gross.str[1:-1])
print(imdb.head())
```

                          title  year                     genres  runtime  rating  metascore    votes   gross
    0  The Shawshank Redemption  1994                      Drama  142 min   9.300     80.000  2295181  28.340
    1           The Dark Knight  2008       Action, Crime, Drama  152 min   9.000     84.000  2259996 534.860
    2                 Inception  2010  Action, Adventure, Sci-Fi  148 min   8.800     74.000  2022025 292.580
    3                Fight Club  1999                      Drama  139 min   8.800     66.000  1819764  37.030
    4              Pulp Fiction  1994               Crime, Drama  154 min   8.900     94.000  1792404 107.930



```python
# 手工添加所有电影类型
gens_set = set()
for g in imdb.genres:
    gens.update(g.split(','))
# 去掉不同的空格
gens_set = {i.strip() for i in gens}
print(gens_set)
```

    {'History', 'Action', 'Sport', 'Biography', 'Mystery', 'Drama', 'Music', 'Romance', 'Family', 'Musical', 'Comedy', 'Horror', 'Animation', 'Adventure', 'Sci-Fi', 'War', 'Crime', 'Western', 'Thriller', 'Fantasy'}
​    


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
# 综合上面的方法，我们可以将代码简化为如下一行
for gen in gens_set:
    imdb[gen] = [1 if gen in i.split(', ') else 0 for movie_gen in imdb.genres]

```


```python
imdb.columns
```




    Index(['title', 'year', 'genres', 'runtime', 'rating', 'metascore', 'votes', 'gross', 'History', 'Action', 'Sport', 'Biography', 'Mystery', 'Drama', 'Music', 'Romance', 'Family', 'Musical', 'Comedy', 'Horror', 'Animation', 'Adventure', 'Sci-Fi', 'War', 'Crime', 'Western', 'Thriller', 'Fantasy'], dtype='object')




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
      <th>History</th>
      <th>Action</th>
      <th>Sport</th>
      <th>Biography</th>
      <th>Mystery</th>
      <th>Drama</th>
      <th>Music</th>
      <th>Romance</th>
      <th>Family</th>
      <th>Musical</th>
      <th>Comedy</th>
      <th>Horror</th>
      <th>Animation</th>
      <th>Adventure</th>
      <th>Sci-Fi</th>
      <th>War</th>
      <th>Crime</th>
      <th>Western</th>
      <th>Thriller</th>
      <th>Fantasy</th>
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
      <td>0</td>
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
      <td>0</td>
      <td>1</td>
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
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <td>1</td>
      <td>1</td>
      <td>0</td>
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
      <td>139 min</td>
      <td>8.800</td>
      <td>66.000</td>
      <td>1819764</td>
      <td>37.030</td>
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
      <td>0</td>
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
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 保存清理后的文件
imdb.to_csv('data/imdb_clean.csv', index=False)
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
    </tr>
    <tr>
      <th>9996</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
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
      <th>9998</th>
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
      <th>9999</th>
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
  </tbody>
</table>
<p>10000 rows × 20 columns</p>
</div>



### Pandas 的字符串向量化操作

非常好用哦！

详细内容及介绍见：
https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html

简单一句话，如果df里面某一栏的值都是字符串，那么可以直接对整行进行操作

```
series.str.lower()
```

支持一切python自带的字符串操作


```python
imdb.title.str.lower()
```




    0       the shawshank redemption
    1                the dark knight
    2                      inception
    3                     fight club
    4                   pulp fiction
                      ...           
    9995                       prowl
    9996          happily ever after
    9997                       cyclo
    9998                 återträffen
    9999                     krugovi
    Name: title, Length: 10000, dtype: object



### pands 字符串向量化操作

除去python自带的字符串操作外，pandas还额外添加了如下的方法：

```
get()
slice()
slice_replace()
cat()
repeat()
normalize()
pad()
wrap()
join()
get_dummies()
```


```python
# 如何将上面的dummies与原有的数据合并？
```

## 数据合并

1. 不同样本，相同属性
   - 抓取数据时，分别保存
   - 不同股票，某个月的数据
   - 合并行，栏不变
   - 上下合并
2. 相同样本，不同属性
   - 来自不同数据源
   - 相同股票，股票数据和基本面数据
   - 以某一栏为准，增加栏
   - 左右合并

### 不同样本，相同属性

同一个专业的同学被分成了两个班上同一门课

```
pd.concat()
df1.append(df2)
```

请尽量不要对拥有重复栏的df做直接的横向合并，尽量保证合并后的df的index,column_name不重复


```python
print(help(pd.concat))
```


```python
# 生成20个fake学生id
stu_ids = ['4101190' + str(i) for i in range(1,10)] + ['410119' + str(i) for i in range(10,21)]
print(stu_ids)
```


```python
# 随机生成经济学两个班的成绩

economics_1 = pd.DataFrame({'stu_ids': stu_ids[:10],
                            'eco_marks': np.random.randint(60,100,size=10)
                           })


economics_2 = pd.DataFrame({'stu_ids': stu_ids[10:],
                            'fin_marks': np.random.randint(60,100,size=10)
                           })
print('Class1','\n', economics_1)
print('Class2','\n', economics_2)
```


```python
# 作为微观经济的老师，请将两个班的成绩合并到一个表格里面，供后期录入系统
```


```python
###-------Concat-----##


```


```python
###---append---####

```


```python
# 

```

### 相同样本，不同属性

需要考虑以下几种情况：

- 相同样本，增加属性
    - 相同专业学生，不同必修课程成绩
- 样本有差异，属性也不同
    - 相同专业学生，不同选修课成绩
    - 每个课程选课的人不同



```
df1.merge(df2)
join
```


```python
print(help(pd.merge))
```


```python
# 随机生成金融学的成绩

finance = pd.DataFrame({'stu_ids': stu_ids,
                            'fin_marks': np.random.randint(60,100,size=20)
                           })
print(finance)
```


```python
# 现在你是学院负责教务的老师需要把金融和经济两门课程的成绩合并起来

#-----------Merge------------###


```


```python
# python和会计课程分别只有一部分同学选修了
python = pd.DataFrame({'stu_ids': random.sample(stu_ids,15),
                            'marks': np.random.randint(80,100,size=15)
                           })
print(python)
accounting = pd.DataFrame({'stu_ids': random.sample(stu_ids,8),
                            'marks': np.random.randint(70,90,size=8)
                           })
print(accounting)
```


```python
# 再来合并看看

```


```python

```

# plotting




```python
# 请尽量使用matplotlib 2.0 以上的版本
import matplotlib
print(matplotlib.__version__)
```


```python
import matplotlib.pyplot as plt
# 下面一行语句的意思是为了让matplotlib可以在notebook里面直接显示图
%matplotlib inline
```


```python

```

### Keep cleaning IMDb data

- votes, year, gross
    - int
- genres
    - get unique genres
    - Use each genre as one column
    - If a movie belongs to the genre, the value should be 1(True), otherwise 0(False)



```python
imdb.votes = imdb.votes.str.replace(',', '').astype(int)
imdb.gross = pd.to_numeric(imdb.gross.str[1:-1])
```


```python
imdb.describe()
```


```python
imdbtitle = imdb.title + imdb.year.str[:-6]
imdbyear = imdb.year.str[-5:-1].astype(int)
imdb.title = imdbtitle.str.strip()
imdb.year = imdbyear
```


```python
imdb.head()
```


```python
imdb.describe()
```


```python
gens = set()
for g in imdb.genres:
    gens.update(g.split(','))
# remove whitespaces
gens = {i.strip() for i in gens}
print(gens)
```


```python
for gg in gens:
    imdb[gg] = [1 if gg in i else 0 for i in imdb.genres ]   
```


```python
imdb.info()
```

### Step 3, Explore Data

#### Global property exploration
做出imdb的描述性统计表格

查看表格，是否有异常？如果存在异常，思考该如何处理


```python
imdb.describe()
```


```python
import numpy as np

```


```python
imdb.loc[803,'gross'] = np.nan
```


```python
imdb.loc[imdb.gross==0,'gross'] = np.nan
```

**练习**
用NaN来替代异常值


```python
imdb.describe()
```


```python
imdb.votes.hist()
```


```python
imdb.loc[imdb.runtime==0, 'runtime'] = np.nan
print(imdb.describe())
```

**练习**
* 查看分数最高、最低的影片
* 查看各个类型电影的数量，评分
* 找出数据中的outlier


```python

```


```python

```

## Plotting

### Matplotlib -- plotting

Python most-used plotting package (http://matplotlib.org/). The package provides a good turtorial with some [example](http://matplotlib.org/users/screenshots.html)


### matplotlib.pyplot

一组命令使得matplotlib运行起来与MATLAB非常相似.
每一个pyplot的function都会对已有的图做一些改变,比如,创建一个图布, 在图布上画图,加图注等等


```python
import matplotlib.pyplot as plt
# 下面一行语句的意思是为了让matplotlib可以在notebook里面直接显示图
%matplotlib inline
```


```python
# Think what the following method has done? how the axes are defined?
plt.plot(range(5,10))
plt.ylabel('Y')
#plt.show()
```


```python
# what will the following codee get? how many lines will be?
plt.plot([1,2,3,4],[5,6,7,8])
```


```python
# use the following code to find the docstring (documentation of the function and method)
print(help(plt.plot))
```

**Exercise**
Try to give labels to the above figure. 'X Values', 'Y labels' for X and Y axis.


```python
plt.show()
```


```python
import numpy as np
x1 = np.array(range(1,5))
```


```python
plt.plot(x1, x1**2, 'ro')
plt.axis([0,6,0,20])
```


```python

```

**Exercise**
Check matplotlib.pyplot [documentation](https://matplotlib.org/api/pyplot_api.html) or use plt.<tab> in ipython console

### Select Different Styles for Matplotlib
Matplotlib allows users to change the style of the figs. Use the code:
```
Plt.style.use(STYLE)
```
Different styles can be found in [Matplotlib Style Gallery](https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html)



```python

```


```python
plt.style.use('fivethirtyeight')
```


```python
plt.plot(range(5))
```

### Alternatives of Matplotlib
There are other packages that can be used instead of matplotlib.
* [seaborn](https://seaborn.pydata.org/), build on matplotlib
* [plotly](https://plot.ly/python/getting-started/)
* [Bokeh](http://bokeh.pydata.org/en/latest/)


```python

```

**After Class Exercise**
- know how to do [subfigs](http://matplotlib.org/examples/pylab_examples/subplot_demo.html)
- learn more of matplotlib via a [simple tutorial](http://www.labri.fr/perso/nrougier/teaching/matplotlib/)
- finish all the exercises in [pyplot tutorial](http://matplotlib.org/1.4.1/users/pyplot_tutorial.html)

### Other Materials

* A simple matplotlib tutorial:
    * http://www.labri.fr/perso/nrougier/teaching/matplotlib/
* Pyplot  Tutorial: http://matplotlib.org/1.4.1/users/pyplot_tutorial.html
* Matplotlib Tutorial: http://matplotlib.org/1.4.1/users/beginner.html
* Introductory slides on scientific visualization, 名为matplotlib-euroscipy-2012.pdf


```python
imdb.metascore.hist()
```
