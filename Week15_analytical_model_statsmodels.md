# Python for Data Science
## Week 15 Analytical Models -- Statsmodles

In this lecture, we will talk about how to use Python to analyze data via statistical models. 
Basically we will provide an overview of the two most commonly used packages in Python **Statsmodles**.

Futhermore, we will also introduce [Stargazer](https://github.com/mwburke/stargazer) for creating regression results tables.

## Statsmodels
> [Statsmodels](http://www.statsmodels.org/stable/) is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. The results are tested against existing statistical packages to ensure that they are correct. 

### An simple example


```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels
# to ensure the figure will be shown inline
%matplotlib inline
```


```python
# change pandas default settings to show more rows and columns of data
# more information please refer to : https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 30)
# surpass the scientific notation
pd.set_option('display.float_format', lambda x: '%.3f' % x)
```


```python
statsmodels.__version__
```

### Basics of the API

通常我们采用如下步骤来使用Statsmodels:

0. 明确你的模型中具体的变量
1. 处理数据Xs & Y(s) 为适合的数据类型。如有需要，用``add_constant()``添加constant.
2. 选择模型
3. 对模型做拟合得到模型的结果 ``model.fit()``
4. 获得模型的summary， ``results.summary()``
5. 如有需要从 results从获取各个参数

### imdB data

用imdb数据做回归分析，探索哪些因素会影响电影的票房？数据集可以在课程中心下载，名字为：

```
imdb_clean.csv
```

### Preview your data


```python
imdb = pd.read_csv('data/imdb_clean.csv')
```


```python
imdb.head()
```


```python
imdb.describe()
```

### Before the model

Check pairwise correlation among the variables

```
df.corr()
```


```python
imdb[['runtime', 'rating', 'metascore', 'votes', 'gross']].corr()
```


```python
imdb.rating
```

### 0. 明确你的模型中具体的变量

下面是我们通常所见的OLS模型的样子，我们需要针对每个项目弄清楚，模型中具体的变量和参数的意义

    $y = \alpha + \beta_1X1 + \beta_2X2 + \epsilon $

比如，对应于imDb的数据，我们的模型可以是：

    $Gross = \alpha + \beta_1rating + \epsilon  $ 

再跑程序/模型之前，你必须要弄清楚模型中每一个参数/变量的意义


```python

```

### 1. 处理数据Xs & Y(s) 为适合的数据类型。如有需要，用``add_constant()``添加constant.


```python
imdbx = imdb.rating
imdby = imdb.gross
print(len(imdbx), len(imdby))
```


```python
imdbX = sm.add_constant(imdbx)
```

### 2. 选择模型


```python
model = sm.OLS(imdby, imdbX, missing='drop')
```

### 3. 对模型做拟合得到模型的结果 ``model.fit()``


```python
res = model.fit()
```

### 4. 获得模型的summary， ``results.summary()``


```python
print(res.summary())
```

### 5. 如有需要从 results从获取各个参数


```python
# get to know results' attributes
dir(res)
```


```python
# params is the 'coef'
results.params

# pvalues is the pvalue
results.pvalues

# try to find R2, t-test, f-test and other parameters that needed
results.rsquared

# t-test explaination: http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLSResults.t_test.html
print(results.tvalues)

results.fittedvalues


```


```python
res.fittedvalues
```

If we add the constant, then need to use the following argeuments, compare the differences

```
print(results.tvalues)
print(results.t_test([1,0]))
print(results.tvalues)
```


```python
res.t_test([1,0])
```

### 多元回归？

    $Gross = \alpha + \beta_1rating + \beta_2runtim + \epsilon  $ 


```python
imdbxs = imdb[['rating', 'runtime']]
imdby = imdb.gross
imdbX = sm.add_constant(imdbxs)
print(len(imdbxs), len(imdby))
```


```python
imdby.describe()
```


```python
model1 = sm.OLS(imdby, imdbX, missing='drop')
res1 = model.fit()
print(res.summary())
```


```python
from stargazer.stargazer import Stargazer as stgz
import seaborn as sns
```


```python
sns.__version__
```


```python
sns.set_theme(color_codes=True)
```


```python
stgz([res,res1])
```


```python
sns.regplot(x="rating", y="gross", data=imdb)
```


```python
sns.lmplot(x="rating", y="gross", data=imdb)
```


```python
import matplotlib.pyplot as plt
plt.plot(imdb['rating'], imdb['gross'], 'ro')
plt.plot(imdb['rating'], res.fittedvalues, 'bo')
```

### 共线性测试

具体细节见文档(https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html)

```
sms.stats.outliers_influence.variance_inflation_factor(exog, exog_idx)
```
第一个参数是Xs的矩阵（np.ndarray），第二个参数是给出对应所想要查看的参数的位置（0，1，2...）


```python
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
```


```python
vif(imdbX.values, 1)
```


```python

```

### Stargazer

一个非常好用的呈现statsmodels回归结果的包。具体信息见：

https://github.com/mwburke/stargazer


```python

```


```python

```

### Seaborn

一个基于matplotlib的包。与Pandas结合的更好，比matplotlib更人性化。可以直接画回归拟合图

见：https://seaborn.pydata.org/tutorial/regression.html


```python

```

### **Exercise**
Use the following exmple to run a simple OLS

**练习**
用下面的数据做回归，需要思考如何建立模型？以及如何呈现结果


数据集来源：

https://vincentarelbundock.github.io/Rdatasets/datasets.html


```python
#url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/MASS/whiteside.csv'
url = 'data/whiteside.csv'
whiteside = pd.read_csv(url)
```


```python
# 练习，添加常数项后，再次运行回归方程，并且得到相关的参数
```


```python
whiteside.drop('Unnamed: 0', axis=1, inplace=True)
```

The description of the data set is or can be found [here](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/doc/MASS/whiteside.html):
> #### Description

> Mr Derek Whiteside of the UK Building Research Station recorded the weekly gas consumption and average external temperature at his own house in south-east England for two heating seasons, one of 26 weeks before, and one of 30 weeks after cavity-wall insulation was installed. The object of the exercise was to assess the effect of the insulation on gas consumption.

> #### Usage

>    whiteside

> #### Format

> The whiteside data frame has 56 rows and 3 columns.:

> - Insul
>   A factor, before or after insulation.
> - Temp
>   Purportedly the average outside temperature in degrees Celsius. (These values is far too low for any 56-week period in the 1960s in South-East England. It might be the weekly average of daily minima.)
> - Gas
>   The weekly gas consumption in 1000s of cubic feet.

> #### Source

> * A data set collected in the 1960s by Mr Derek Whiteside of the UK Building Research Station. Reported by

> * Hand, D. J., Daly, F., McConway, K., Lunn, D. and Ostrowski, E. eds (1993) A Handbook of Small Data Sets. Chapman & Hall, p. 69.

> #### References

> * Venables, W. N. and Ripley, B. D. (2002) Modern Applied Statistics with S. Fourth edition. Springer.


这个数据集共56行，3列。包含，是否使用了保暖层、温度、燃气用量

#### Fitting the model
我们的目的是了解在保温(Insul)前后的效果及燃气（Gas）的使用量变化。

因此，首先我们了解一下在保温之前Gas与Temp之间的关系，在做之前先想想我们有可能会得到什么结果？

试做一个回归分析，并思考结果是否跟我们期待的一致？

**Approach 1**
Run two OLS models on data with insul and without insul repectively, and compare the results.

**Approach 2**
Run one OLS model and add insul as a dummy varibale.


```python
Before = whiteside[whiteside.Insul=='Before']
After = whiteside[whiteside.Insul=='After']
```


```python
whiteside['ins_dummy'] = [0 if i == 'Before' else 1 for i in whiteside.Insul]
```


```python
whiteside.head()
```


```python
def callols(dat, xcols, ycol, constant=True):
    """
    param: dat, the dataframe fro use of ols
    param: xcols, coulmn names for indenpendent variables
    param: ycol, column name for dependent variable
    param: constant, add constant or not. Default True
    """
    x = dat[xcols]
    if constant:
        x = sm.add_constant(x)

    model = sm.OLS(dat[ycol], x)
    results = model.fit()
    print(results.summary())
    return results
```


```python
resbefore = callols(Before, 'Temp', 'Gas')
```


```python
resafter = callols(After, 'Temp', 'Gas')
```

### How should we presents results?

| | Model 1 (before) | Model 2 (After)|
|---------|--------|------|
|Temp Coef|-0.3932 |-0.2779 |
|Temp p-value|0.000 | 0.000|
|Temp std err|0.020 | 0.025|
|R^2|  0.944 |0.813 |



```python
stgz([resbefore, resafter])
```

Plot data and fit


```python
sns.lmplot(x="Temp", y="Gas", data=Before)
```


```python
sns.lmplot(x="Temp", y="Gas", data=After)
```


```python
# Think whether you can revise the function to be more generalized
def plotres(dat, res):
    """
    plot ols results
    param: dat, dataframe
    param: res, ols result object
    """
    plt.plot(dat["Temp"], dat["Gas"], 'ro')
    plt.plot(dat["Temp"], res.fittedvalues, 'b')
    plt.axis([-2,12,0,10])
    plt.legend(['Data', 'Fitted model'])
    plt.xlabel('Temperature')
    plt.ylabel('Gas')
    # plt.title('Before Insulation')
#     plt.show()
#     plt.close()
```


```python
import matplotlib.pyplot as plt
plt.axis
plotres(Before, resbefore)
```

再回归保温后的数据看看


```python
resafter = callols(After, 'Temp', 'Gas')
```


```python
plotres(After, resafter)
```

### OLS Approach 2


```python
whiteside['ins_ind'] = [0 if i=='Before' else 1 for i in whiteside.Insul]
```


```python
x = sm.add_constant(whiteside[['Temp', 'ins_dummy']])
model = sm.OLS(whiteside['Gas'], x)

res_all = model.fit()
print(res_all.summary())
```


```python

```


```python

```


```python

```

下述方法可以获取结果中的主要参数


```python

```


```python
# 练习，添加常数项后，再次运行回归方程，并且得到相关的参数
```
