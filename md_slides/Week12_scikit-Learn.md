# Python for Data Analysis
## Week 12 Scikit-Learn Package
This lecture will talk about how to use Python to analyze data. Basically we will provide an overview of the two most commonly used packages in Python **scikit-learn** package

## Scikit-learn
>[SciKits](http://scikit-learn.org/stable/documentation.html) is a set of simple and efficient tools for data mining and data analysis

Some resources on machine learning and Scikit-learn:
* https://www.apprendimentoautomatico.it/en/machine-learning-best-cheat-sheets-one-page/
* http://usblogs.pwc.com/emerging-technology/machine-learning-methods-infographic/

The Scikit-Learn API is designed with the following guiding principles in mind, as outlined in the [Scikit-Learn API paper](http://arxiv.org/abs/1309.0238):

- *Consistency*: All objects share a common interface drawn from a limited set of methods, with consistent documentation.

- *Inspection*: All specified parameter values are exposed as public attributes.

- *Limited object hierarchy*: Only algorithms are represented by Python classes; datasets are represented
  in standard formats (NumPy arrays, Pandas ``DataFrame``s, SciPy sparse matrices) and parameter
  names use standard Python strings.

- *Composition*: Many machine learning tasks can be expressed as sequences of more fundamental algorithms,
  and Scikit-Learn makes use of this wherever possible.

- *Sensible defaults*: When models require user-specified parameters, the library defines an appropriate default value.

In practice, these principles make Scikit-Learn very easy to use, once the basic principles are understood.
Every machine learning algorithm in Scikit-Learn is implemented via the Estimator API, which provides a consistent interface for a wide range of machine learning applications.

## 获取数据
Scikit-Learn本身提供了几个在数据挖掘和机器学习领域较为常见的数据集。这些数据集可以通过Scikit-Learn 的 [datesets API](http://scikit-learn.org/stable/datasets/index.html) 来调取


```python
# import datasets API from scikit-learn
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
```


```python
iris = datasets.load_iris()
```


```python
# check what kind of methods does 'digits' object has
# can use TAB as well
# try all the methods/attributes
dir(iris)
```


```python
iris['target'].shape
```


```python
print(iris.DESCR) # or print(iris['DESCR'])
```


```python
print(iris.DESCR)
```

### 练习
1. 从scikit-learn获取 digits, diabets数据集
2. 查看数据集的说明、features,targets,etc


```python
digits = datasets.load_digits()
# Isolate the `digits` data
digits_data = digits.data

# Inspect the shape
print(digits_data.shape)

# Isolate the target values with `target`
digits_target = digits.target

# Inspect the shape
print(digits_target.shape)

# Print the number of unique labels
number_digits = len(np.unique(digits.target))

# Isolate the `images`
digits_images = digits.images

# Inspect the shape
print(digits_images.shape)
```

    (1797, 64)
    (1797,)
    (1797, 8, 8)



```python
digits.data
```




    array([[ 0.,  0.,  5., ...,  0.,  0.,  0.],
           [ 0.,  0.,  0., ..., 10.,  0.,  0.],
           [ 0.,  0.,  0., ..., 16.,  9.,  0.],
           ...,
           [ 0.,  0.,  1., ...,  6.,  0.,  0.],
           [ 0.,  0.,  2., ..., 12.,  0.,  0.],
           [ 0.,  0., 10., ..., 12.,  1.,  0.]])




```python
# Import matplotlib
import matplotlib.pyplot as plt

# Figure size (width, height) in inches
fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    # Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

# Show the plot
plt.show()
```


​    
![png](output_13_0.png)
​    



```python
diabetes = datasets.load_diabetes()
```

## Seaborn package
seaborn package provides a better looking matplotlib plotting. And it provides some sample datasets as well



```python
import seaborn as sns
# similarly seaborn provides the some datasets too
iris2 = sns.load_dataset('iris')
iris2.head()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic = sns.load_dataset('titanic')
titanic.head()
```


```python
help(sns.load_dataset)
```

### 练习

seaborn是否有digits数据集？如何了解seaborn都提供哪些数据集？


```python

```

### 练习

Seaborn 和 Scikit-Learn的数据集的差别是什么？


```python

```

### What are features and samples
How to get features, targets and samples from both datasets?


```python
iris2.info()
```


```python
# get features, targets and samples from iris
X_iris = iris2.iloc[:,:4]
y_iris = iris2['species']
# print(y_iris)
```


```python
print(X_iris.head())
print(y_iris.head())
```

       sepal_length  sepal_width  petal_length  petal_width
    0           5.1          3.5           1.4          0.2
    1           4.9          3.0           1.4          0.2
    2           4.7          3.2           1.3          0.2
    3           4.6          3.1           1.5          0.2
    4           5.0          3.6           1.4          0.2
    0    setosa
    1    setosa
    2    setosa
    3    setosa
    4    setosa
    Name: species, dtype: object



```python
iris2.head()
```

### Basics of the API

通常来说，一般采用如下几个步骤来使用Scikit-Learn:
1. 选择一个合适的模型
2. 设置模型的相关参数
3. 把数据整合为一个feature matrix和一个target vector. Scikit-Learn通常只接受 NumPy arrays, Pandas ``DataFrame``s, SciPy sparse matrices 几种数据类型
4. 调用``fit()``模型拟合
5. 把模型应用到新的数据上
    - 对于有监督学习来说，我们一般调用``predict()``方法
    - 对无监督学习，我们则调用``transform()``或``predict()``

**用IRIS数据集来做一个有监督的classification**


```python
from sklearn.model_selection import train_test_split
train_test_split?
```


```python
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris)
```


```python
X_train.head()
```


```python
len(x_test)
```


```python

```

### 练习

- 默认的train/test各占百分之多少？
- 如何修改train/test的百分比？
- 如何获取train/validation/test 三个数据集


```python
# change test/train set percentage
# train_test_split(X_iris, y_iris, test_size=0.1)

# #get train/validation/test set
# xtrain, x_set, ytrain, y_set = train_test_split(X_iris, y_iris)
# xvalidation, x_test, yvalidation, y_test = train_test_split(x_set, y_set)
```

## 课后
了解cross_validation.


```python

```


```python
from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB()                       # 2. instantiate model
model.fit(X_train, y_train)                  # 3. fit model to data
y_model = model.predict(X_test)             # 4. predict on new data
```


```python
model.predict(X_test)
```




    array(['versicolor', 'versicolor', 'virginica', 'versicolor',
           'versicolor', 'versicolor', 'versicolor', 'virginica', 'setosa',
           'virginica', 'setosa', 'versicolor', 'virginica', 'versicolor',
           'virginica', 'versicolor', 'setosa', 'versicolor', 'virginica',
           'versicolor', 'virginica', 'versicolor', 'setosa', 'virginica',
           'virginica', 'versicolor', 'virginica', 'virginica', 'virginica',
           'versicolor', 'setosa', 'virginica', 'setosa', 'setosa',
           'versicolor', 'virginica', 'virginica', 'virginica'], dtype='<U10')




```python
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_model)
```




    0.9210526315789473



如何输入一个X，得到相关的预测结果？


```python
model.predict(X_test.iloc[0].values.reshape(1,-1))
```




    array(['versicolor'], dtype='<U10')



**练习**

用IRIS数据集来做一个无监督的clustering


```python
from sklearn.cluster import KMeans      # 1. Choose the model class
```


```python
model = KMeans(n_clusters=3)  # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                    # 3. Fit to data. Notice y is not specified!
y_kmeans = model.predict(X_iris)        # 4. Determine cluster labels
```


```python
y_kmeans
```


```python
iris2['cluster'] = y_kmeans
colors = {0:'blue', 1:'red', 2:'green'}
```


```python
iris2.head()
```

**画图把不同的cluster用不同颜色表示出来**


```python
# plott = plt.figure()

fig, ax = plt.subplots()

grouped = iris2.groupby('cluster')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='petal_length', y='petal_width', label=key, color=colors[key])

plt.show()
```


```python
fig, ax = plt.subplots()
colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}
grouped = iris2.groupby('species')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='petal_length', y='petal_width', label=key, color=colors[key])

plt.show()
```


```python
sns.lmplot("petal_length", "petal_width", data=iris2, hue='species',
           col='cluster', fit_reg=False)
plt.show()
```

**练习**

尝试用linear model 对diabets数据进行分析


```python
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
```


```python
# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

**课后练习**

尝试用linear model 对imdb数据进行分析


```python
import pandas as pd
imdb = pd.read_csv('data/imdb_clean.csv')
imdb.head()
```


```python
genres_set = set([j for i in imdb.genres for j in i.split(', ') ])

for g in genres_set:
    imdb[g] = [1 if g in i.split(', ') else 0 for i in imdb.genres]

imdb['votes'] = [int(''.join(i.split(','))) for i in imdb.votes]

imdb.dropna(inplace=True)
imdb.drop_duplicates('title', inplace=True)

imdb.columns
```


```python
imdb_x = imdb[['year', 'runtime', 'rating', 'metascore', 'votes',
       'Thriller', 'Fantasy', 'Western', 'Biography',
       'Drama', 'Music', 'Sport', 'Horror', 'Sci-Fi', 'History', 'Animation',
       'Action', 'Musical', 'Comedy', 'Family', 'Mystery', 'War', 'Romance',
       'Crime', 'Adventure']]
imdb_y = imdb['gross_million']
```


```python
X_train_imdb, X_test_imdb, y_train_imdb, y_test_imdb = train_test_split(imdb_x, imdb_y)
```


```python
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train_imdb, y_train_imdb,)

# Make predictions using the testing set
imdb_y_pred = regr.predict(X_test_imdb)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test_imdb, imdb_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test_imdb, imdb_y_pred))
```


```python

```


```python

```
