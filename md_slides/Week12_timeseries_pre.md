# Python for Data Analysis

课程内容：

1. 处理时间序列
2. 数据可视化

# 处理时间序列
由于 Pandas 最初是为金融模型而创建的，因此它拥有一些功能非常强大的日期、时间、带时间索引数据的处理工具。日期与时间数据主要包含三类：
* 时间戳表示某个具体的时间点（例如 2018 年 12 月 16 日上午 7点）。
* 时间间隔与周期表示开始时间点与结束时间点之间的时间长度，例如 2018 年（指的是 2018 年 1 月 1 日至 2018 年 12 月 31 日这段时间间隔）。周期通常是指一种特殊形式的时间间隔，每个间隔长度相同，彼此之间不会重叠（例如，以 24 小时为周期构成每一天）。
* 时间增量（time delta）或持续时间（duration）表示精确的时间长度（例如，某程序运行持续时间 22.56 秒）。

## 1. Python的日期与时间工具

在 Python 标准库与第三方库中有许多可以表示日期、时间、时间增量和时间跨度（timespan）的工具。尽管 Pandas 提供的时间序列工具更适合用来处理数据科学问题，但是了解 Pandas 与 Python 标准库以及第三方库中的其他时间序列工具之间的关联性将大有裨益。

## 原生Python的日期与时间工具：datetime

Python 基本的日期与时间功能都在标准库的 datetime 模块中。


```python
# Python自带datetime 库 介绍
from datetime import datetime as dt
from datetime import timedelta as tmdlt
help(dt)
```

    Help on class datetime in module datetime:
    
    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |  
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |  
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |  
     |  ctime(...)
     |      Return ctime() style string.
     |  
     |  date(...)
     |      Return date object with same year, month and day.
     |  
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |  
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |      timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').
     |  
     |  replace(...)
     |      Return datetime with new specified fields.
     |  
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |  
     |  timestamp(...)
     |      Return POSIX timestamp as float.
     |  
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |  
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |  
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |  
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |  
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |  
     |  fromisoformat(...) from builtins.type
     |      string -> datetime from datetime.isoformat() output
     |  
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |  
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |      
     |        tz
     |          Timezone object.
     |      
     |      If no tz is specified, uses local timezone.
     |  
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |  
     |  utcfromtimestamp(...) from builtins.type
     |      Construct a naive UTC datetime from a POSIX timestamp.
     |  
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  fold
     |  
     |  hour
     |  
     |  microsecond
     |  
     |  minute
     |  
     |  second
     |  
     |  tzinfo
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |  
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |  
     |  resolution = datetime.timedelta(microseconds=1)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |  
     |  __format__(...)
     |      Formats self with strftime.
     |  
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |  
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  
     |  strftime(...)
     |      format -> strftime() style string.
     |  
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |  
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from date:
     |  
     |  fromisocalendar(...) from builtins.type
     |      int, int, int -> Construct a date from the ISO year, week number and weekday.
     |      
     |      This is the inverse of the date.isocalendar() function
     |  
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |  
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |  
     |  day
     |  
     |  month
     |  
     |  year
    
    

### 用 datetime 类型创建一个日期


```python
# 获取现在日期和时间
now = dt.today()
print(now)
print(type(now))
```

    2020-11-23 20:09:46.629049
    <class 'datetime.datetime'>
    


```python
# 生成一个日期
dt(year=2018, month=12, day=16)
```




    datetime.datetime(2018, 12, 16, 0, 0)




```python
# 明天的此时此刻
now + 1
```


```python
# timedelta 时间间隔
help(tmdlt)
```

    Help on class timedelta in module datetime:
    
    class timedelta(builtins.object)
     |  Difference between two datetime values.
     |  
     |  timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
     |  
     |  All arguments are optional and default to 0.
     |  Arguments may be integers or floats, and may be positive or negative.
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  total_seconds(...)
     |      Total seconds in the duration.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  days
     |      Number of days.
     |  
     |  microseconds
     |      Number of microseconds (>= 0 and less than 1 second).
     |  
     |  seconds
     |      Number of seconds (>= 0 and less than 1 day).
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  max = datetime.timedelta(days=999999999, seconds=86399, microseconds=9...
     |  
     |  min = datetime.timedelta(days=-999999999)
     |  
     |  resolution = datetime.timedelta(microseconds=1)
    
    

#### 练习

计算 2000年1月20日 100天后，日期是哪天？


### 将不同格式的日期输入、输出

两个作用完全相反的方法：

- strftime(format), 日期--> 字符串，将时间日期数据，按照要求的格式输出为字符串

- strptime(date_string, format)，字符串--> 日期，将不同格式的字符串生成一个时间日期数据


```python
# 今天是星期几
now.strftime('%A')
```




    'Monday'




```python
# 用 yyyymmdd格式显示今天日期

```




    '20201123'



在最后一行代码中，为了打印出是星期几，我们使用了一个标准字符串格式（standard string format）代码 "%A"，你可以在 Python 的datetime 文档（https://docs.python.org/3/library/datetime.html ）的“strftime”节（https://docs.python.org/3/library/datetime.html#strftime-and-strptimebehavior ）查看具体信息。

#### 练习

1. 分别用以下格式生成一个日期时间类型时间

```
2020,05,07
18 Jan 1990
1992/May/7, 07:58
```

2. 将上述最后一个时间日期，以下面的格式print出来

XX年X月X日，X点X分


```python

```


```python

```




    '1992年05月07日, 7点58分'



#### 几个常用的Python第三方日期时间包

由于时间关系本课程不做介绍，可自学

1. 第三方库 dateutil 也是一个针对日期和时间进行处理的package,可以与datetime 模块搭配使用，可以快速实现许多处理日期与时间的功能。 关于 dateutil 的其他日期功能可以通过 dateutil 的在线文档（http://labix.org/python-dateutil ）学习。
2. 还有一个值得关注的程序包是 pytz（http://pytz.sourceforge.net/ ），这个工具解决了绝大多数时间序列数据都会遇到的难题：时区。

### NumPy时间序列类型

datetime 和 dateutil 模块在灵活性与易用性方面都表现出色，
你可以用这些对象及其相应的方法轻松完成你感兴趣的任意操作。
但如果你处理的时间数据量比较大，那么速度就会比较慢。就像之
前介绍过的 Python 的原生列表对象没有 NumPy 中已经被编码的数
值类型数组的性能好一样，Python 的原生日期对象同样也没有
NumPy 中已经被编码的日期（encoded dates）类型数组的性能好。

Python 原生日期格式的性能弱点促使 NumPy 团队为 NumPy 增加了
自己的时间序列类型。 datetime64 类型将日期编码为 64 位整
数，这样可以让日期数组非常紧凑（节省内存）。 datetime64 需
要在设置日期时确定具体的输入类型：


```python
import numpy as np
date = np.array('2018-12-16', dtype=np.datetime64)
# date = np.array('2018-12-16')
date
```




    array('2018-12-16', dtype='datetime64[D]')



只要有了这个日期格式，就可以进行快速的向量化运算：


```python
date + np.arange(20)
```




    array(['2018-12-16', '2018-12-17', '2018-12-18', '2018-12-19',
           '2018-12-20', '2018-12-21', '2018-12-22', '2018-12-23',
           '2018-12-24', '2018-12-25', '2018-12-26', '2018-12-27',
           '2018-12-28', '2018-12-29', '2018-12-30', '2018-12-31',
           '2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04'],
          dtype='datetime64[D]')



因为 NumPy 的 datetime64 数组内元素的类型是统一的，所以这种数组的运算速度会比 Python 的 datetime 对象的运算速度快很多，尤其是在处理较大数组时。

datetime64 与 timedelta64 对象的一个共同特点是，它们都是在基本时间单位（fundamental time unit）的基础上建立的。由于datetime64 对象是 64 位精度，所以可编码的时间范围可以是基本单元的 2**64 倍。也就是说，datetime64 在时间精度（time resolution）与最大时间跨度（maximum time span）之间达成了一种平衡。

比如你想要一个时间纳秒（nanosecond，ns）级的时间精度，那么你就可以将时间编码到 0~264 纳秒或 600 年之内，NumPy 会自动判断输入时间需要使用的时间单位。例如，下面是一个以天为单位的日期：


```python
np.datetime64('2020-03-16')
```




    numpy.datetime64('2020-03-16')



而这是一个以分钟为单位的日期：


```python
np.datetime64('2020-03-16 12:00')
```




    numpy.datetime64('2020-03-16T12:00')



需要注意的是，时区将自动设置为执行代码的操作系统的当地时区。你可以通过各种格式的代码设置基本时间单位。例如，将时间单位设置为纳秒：


```python
np.datetime64('2018-12-16 12:59:59.50', 'ns')
```




    numpy.datetime64('2018-12-16T12:59:59.500000000')



NumPy 的 datetime64 文档（http://docs.scipy.org/doc/numpy/reference/arrays.datetime.html ）总结了所有支持相对与绝对时间跨度的时间与日期单位格式代码，下表对此总结如下：

代码|含义|时间跨度 (相对)| 时间跨度 (绝对)
-------- | ----------- |-------- |--------  
Y| 年（year）| ± 9.2e18 |年[9.2e18 BC, 9.2e18 AD]
M| 月（month）| ± 7.6e17 |年[7.6e17 BC, 7.6e17 AD]
W|周（week）| ± 1.7e17| 年[1.7e17 BC, 1.7e17 AD]
D| 日（day）| ± 2.5e16 |年[2.5e16 BC, 2.5e16 AD]
h| 时（hour）| ± 1.0e15|年[1.0e15 BC, 1.0e15 AD]
m| 分（minute）| ± 1.7e13| 年[1.7e13 BC, 1.7e13 AD]
s| 秒（second）| ± 2.9e12 |年[ 2.9e9 BC, 2.9e9 AD]
ms| 毫秒（millisecond）| ± 2.9e9 |年[ 2.9e6 BC, 2.9e6 AD]
us| 微秒（microsecond）| ± 2.9e6| 年[290301 BC, 294241 AD]
ns| 纳秒（nanosecond）| ± 292 |年[ 1678 AD, 2262 AD]
ps| 皮秒（picosecond）| ± 106 |天[ 1969 AD, 1970 AD]
fs| 飞秒（femtosecond）| ± 2.6 |小时[ 1969 AD, 1970 AD]
as| 原秒（attosecond）| ± 9.2| 秒[ 1969 AD, 1970 AD]

对于日常工作中的时间数据类型，默认单位都用纳秒datetime64[ns]，因为用它来表示时间范围精度可以满足绝大部分需求。

### Pandas的日期与时间工具：理想与现实的最佳解决方案
Pandas 所有关于日期与时间的处理方法全部都是通过 Timestamp对象实现的，它利用 numpy.datetime64 的有效存储和向量化接口将 datetime 和 dateutil 的易用性有机结合起来。Pandas 通过一组 Timestamp 对象就可以创建一个可以作为 Series 或DataFrame 索引的 DatetimeIndex，我们将在后面介绍许多类似的例子。

具体教程参见：https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

例如，可以用 Pandas 的方式演示前面介绍的日期与时间功能。我们可以灵活处理不同格式的日期与时间字符串，获取某一天是星期几：


```python
import pandas as pd
date = pd.to_datetime("16th of December, 2018")
date
```




    Timestamp('2018-12-16 00:00:00')




```python
date.strftime('%A')
```




    'Sunday'



另外，也可以直接进行 NumPy 类型的向量化运算：


```python
date + pd.to_timedelta(np.arange(12), 'D')
```




    DatetimeIndex(['2018-12-16', '2018-12-17', '2018-12-18', '2018-12-19',
                   '2018-12-20', '2018-12-21', '2018-12-22', '2018-12-23',
                   '2018-12-24', '2018-12-25', '2018-12-26', '2018-12-27'],
                  dtype='datetime64[ns]', freq=None)



## 2. Pandas时间序列：用时间作索引
Pandas 时间序列工具非常适合用来处理带时间戳的索引数据。例如，我们可以通过一个时间索引数据创建一个 Series 对象：


```python
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04','2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
data
```




    2014-07-04    0
    2014-08-04    1
    2015-07-04    2
    2015-08-04    3
    dtype: int64



有了一个带时间索引的 Series 之后，就能用它来演示之前介绍过的Series 取值方法，可以直接用日期进行切片取值：


```python
data['2014-07-04':'2015-07-04']
```




    2014-07-04    0
    2014-08-04    1
    2015-07-04    2
    dtype: int64



另外，还有一些仅在此类 Series 上可用的取值操作，例如直接通过年份切片获取该年的数据：


```python
data['2015']
```




    2015-07-04    2
    2015-08-04    3
    dtype: int64




```python
import tushare as ts
stockDF = ts.get_hist_data('603970', start='2018-01-01')
```

    本接口即将停止更新，请尽快使用Pro版接口：https://waditu.com/document/2
    

#### tushare package

是国内较早也较为完整的一个股票市场相关信息包。上面所展示的数据获取，是通过他们的普通接口来获取的，但是近期，普通API已经不再维护（仍然可用）。

如果使用较多的话，建议注册（免费）采用pro接口，具体信息见：https://waditu.com/

两个接口代码略有不同，

```
pro = ts.pro_api(字符串形式的token)
stockDF = pro.daily(ts_code='603970.SH', start_date='20190701')
```


```python
stockDF
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
      <th>open</th>
      <th>high</th>
      <th>close</th>
      <th>low</th>
      <th>volume</th>
      <th>price_change</th>
      <th>p_change</th>
      <th>ma5</th>
      <th>ma10</th>
      <th>ma20</th>
      <th>v_ma5</th>
      <th>v_ma10</th>
      <th>v_ma20</th>
      <th>turnover</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-11-23</th>
      <td>19.09</td>
      <td>19.88</td>
      <td>19.70</td>
      <td>19.00</td>
      <td>53169.93</td>
      <td>0.62</td>
      <td>3.25</td>
      <td>18.856</td>
      <td>18.154</td>
      <td>17.226</td>
      <td>68702.48</td>
      <td>54169.32</td>
      <td>35019.81</td>
      <td>5.57</td>
    </tr>
    <tr>
      <th>2020-11-20</th>
      <td>18.76</td>
      <td>19.30</td>
      <td>19.08</td>
      <td>18.60</td>
      <td>39240.23</td>
      <td>0.08</td>
      <td>0.42</td>
      <td>18.486</td>
      <td>17.815</td>
      <td>17.050</td>
      <td>66352.32</td>
      <td>50819.03</td>
      <td>33059.17</td>
      <td>4.11</td>
    </tr>
    <tr>
      <th>2020-11-19</th>
      <td>18.82</td>
      <td>20.00</td>
      <td>19.00</td>
      <td>18.56</td>
      <td>100417.93</td>
      <td>0.12</td>
      <td>0.64</td>
      <td>18.156</td>
      <td>17.530</td>
      <td>16.920</td>
      <td>64471.80</td>
      <td>48480.01</td>
      <td>31894.37</td>
      <td>10.51</td>
    </tr>
    <tr>
      <th>2020-11-18</th>
      <td>17.50</td>
      <td>18.88</td>
      <td>18.88</td>
      <td>17.45</td>
      <td>72634.04</td>
      <td>1.26</td>
      <td>7.15</td>
      <td>17.820</td>
      <td>17.248</td>
      <td>16.792</td>
      <td>50111.13</td>
      <td>39572.82</td>
      <td>27368.06</td>
      <td>7.60</td>
    </tr>
    <tr>
      <th>2020-11-17</th>
      <td>17.80</td>
      <td>18.15</td>
      <td>17.62</td>
      <td>17.02</td>
      <td>78050.25</td>
      <td>-0.23</td>
      <td>-1.29</td>
      <td>17.486</td>
      <td>16.939</td>
      <td>16.683</td>
      <td>43096.10</td>
      <td>33380.46</td>
      <td>24453.81</td>
      <td>8.17</td>
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
    </tr>
    <tr>
      <th>2018-06-01</th>
      <td>26.55</td>
      <td>27.90</td>
      <td>26.35</td>
      <td>26.30</td>
      <td>72053.98</td>
      <td>0.22</td>
      <td>0.84</td>
      <td>26.744</td>
      <td>26.744</td>
      <td>26.744</td>
      <td>67268.16</td>
      <td>67268.16</td>
      <td>67268.16</td>
      <td>21.62</td>
    </tr>
    <tr>
      <th>2018-05-31</th>
      <td>25.01</td>
      <td>26.35</td>
      <td>26.16</td>
      <td>25.01</td>
      <td>75553.66</td>
      <td>-0.97</td>
      <td>-3.58</td>
      <td>26.843</td>
      <td>26.843</td>
      <td>26.843</td>
      <td>66071.70</td>
      <td>66071.70</td>
      <td>66071.70</td>
      <td>22.67</td>
    </tr>
    <tr>
      <th>2018-05-30</th>
      <td>27.45</td>
      <td>28.98</td>
      <td>27.11</td>
      <td>27.03</td>
      <td>109443.12</td>
      <td>-0.04</td>
      <td>-0.15</td>
      <td>27.070</td>
      <td>27.070</td>
      <td>27.070</td>
      <td>62911.05</td>
      <td>62911.05</td>
      <td>62911.05</td>
      <td>32.83</td>
    </tr>
    <tr>
      <th>2018-05-29</th>
      <td>26.79</td>
      <td>27.79</td>
      <td>27.06</td>
      <td>26.28</td>
      <td>38311.70</td>
      <td>0.03</td>
      <td>0.11</td>
      <td>27.050</td>
      <td>27.050</td>
      <td>27.050</td>
      <td>39645.01</td>
      <td>39645.01</td>
      <td>39645.01</td>
      <td>11.49</td>
    </tr>
    <tr>
      <th>2018-05-28</th>
      <td>27.71</td>
      <td>28.13</td>
      <td>27.04</td>
      <td>26.81</td>
      <td>40978.32</td>
      <td>-0.60</td>
      <td>-2.17</td>
      <td>27.040</td>
      <td>27.040</td>
      <td>27.040</td>
      <td>40978.32</td>
      <td>40978.32</td>
      <td>40978.32</td>
      <td>12.29</td>
    </tr>
  </tbody>
</table>
<p>607 rows × 14 columns</p>
</div>




```python
stockDF['2018'] # will return error
```

#### 练习

将stockDF的index修改为datetime数据类型


```python

```


```python

```

## 3. Pandas时间序列数据结构
这里将介绍 Pandas 用来处理时间序列的基础数据类型。
* 针对时间戳数据，Pandas 提供了 <font color=red>Timestamp</font> 类型。与前面介绍的一样，它本质上是 Python 的原生 datetime 类型的替代品，但是在性能更好的 numpy.datetime64 类型的基础上创建。对应的索引数据结构是 DatetimeIndex。
* 针对时间周期数据，Pandas 提供了 <font color=red>Period</font> 类型。这是利用numpy.datetime64 类型将固定频率的时间间隔进行编码。对应的索引数据结构是 PeriodIndex。
* 针对时间增量或持续时间，Pandas 提供了 <font color=red>Timedelta</font> 类型。Timedelta 是一种代替 Python 原生 datetime.timedelta 类型的高性能数据结构，同样是基于 numpy.timedelta64 类型。对应的索引数据结构是 TimedeltaIndex。

最基础的日期 / 时间对象是 Timestamp 和 DatetimeIndex。这两种对象可以直接使用，最常用的方法是 pd.to_datetime() 函数，它可以解析许多日期与时间格式。对 pd.to_datetime() 传递一个日期会返回一个 Timestamp 类型，传递一个时间序列会返回一个DatetimeIndex 类型：


```python
dates = pd.to_datetime([dt(2015, 7, 3), 
                        '4th of July, 2015','2015-Jul-6', 
                        '07-07-2015', '20150708'])
dates
```




    DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-06', '2015-07-07',
                   '2015-07-08'],
                  dtype='datetime64[ns]', freq=None)



任何 DatetimeIndex 类型都可以通过 to_period() 方法和一个频率代码转换成 PeriodIndex 类型。下面用 'D' 将数据转换成单日的时间序列：


```python
dates.to_period('D')
```




    PeriodIndex(['2015-07-03', '2015-07-04', '2015-07-06', '2015-07-07',
                 '2015-07-08'],
                dtype='period[D]', freq='D')



当用一个日期减去另一个日期时，返回的结果是 TimedeltaIndex 类型：


```python
dates - dates[0]
```




    TimedeltaIndex(['0 days', '1 days', '3 days', '4 days', '5 days'], dtype='timedelta64[ns]', freq=None)



为了能更简便地创建有规律的时间序列，Pandas 提供了一些方法：pd.date_range() 可以处理时间戳、pd.period_range() 可以处理周期、pd.timedelta_range() 可以处理时间间隔。我们已经知道，Python 的 range() 和 NumPy 的 np.arange() 可以用起点、终点和步长（可选的）创建一个序列。pd.date_range() 与之类似，通过开始日期、结束日期和频率代码（同样是可选的）创建一个有规律的日期序列，默认的频率是天：


```python
pd.date_range('2015-07-03', '2015-07-10')
```




    DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-05', '2015-07-06',
                   '2015-07-07', '2015-07-08', '2015-07-09', '2015-07-10'],
                  dtype='datetime64[ns]', freq='D')



此外，日期范围不一定非是开始时间与结束时间，也可以是开始时间与周期数 periods：


```python
pd.date_range('2015-07-03', periods=8)
```




    DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-05', '2015-07-06',
                   '2015-07-07', '2015-07-08', '2015-07-09', '2015-07-10'],
                  dtype='datetime64[ns]', freq='D')



你可以通过 freq 参数改变时间间隔，默认值是 D。例如，可以创建一个按小时变化的时间戳：


```python
pd.date_range('2015-07-03', periods=8, freq='H')
```




    DatetimeIndex(['2015-07-03 00:00:00', '2015-07-03 01:00:00',
                   '2015-07-03 02:00:00', '2015-07-03 03:00:00',
                   '2015-07-03 04:00:00', '2015-07-03 05:00:00',
                   '2015-07-03 06:00:00', '2015-07-03 07:00:00'],
                  dtype='datetime64[ns]', freq='H')



如果要创建一个有规律的周期或时间间隔序列，有类似的函数pd.period_range() 和 pd.timedelta_range()。下面是一个以月为周期的示例：


```python
pd.period_range('2015-07', periods=8, freq='M')
```




    PeriodIndex(['2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12',
                 '2016-01', '2016-02'],
                dtype='period[M]', freq='M')



以及一个以小时递增的序列：


```python
pd.timedelta_range(0, periods=10, freq='H')
```




    TimedeltaIndex(['00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00',
                    '05:00:00', '06:00:00', '07:00:00', '08:00:00', '09:00:00'],
                   dtype='timedelta64[ns]', freq='H')



## 4. 时间频率与偏移量
Pandas 时间序列工具的基础是时间频率或偏移量（offset）代码。就像之前见过的 D（day）和 H（hour）代码，我们可以用这些代码设置任意需要的时间间隔。下表总结了主要的频率代码：

代码| 描述| 代码| 描述
----|----|----|----
D|天（calendar day，按日历算，含双休日）| B| 天（business day，仅含工作日）
W |周（weekly）
M |月末（month end）| BM|月末（business month end，仅含工作日）
Q |季末（quarter end）| BQ|季末（business quarter end，仅含工作日）
A| 年末（year end）| BA|年末（business year end，仅含工作日）
H |小时（hours）| BH|小时（business hours，工作时间）
T |分钟（minutes）
S |秒（seconds）
L |毫秒（milliseonds）
U |微秒（microseconds）
N |纳秒（nanoseconds）

月、季、年频率都是具体周期的结束时间（月末、季末、年末），而有一些以 S（start，开始）为后缀的代码表示日期开始（如下表所示）。

代码|频率
----|----
MS| 月初（month start）
BMS| 月初（business month start，仅含工作日）
QS| 季初（quarter start）
BQS| 季初（business quarter start，仅含工作日）
AS| 年初（year start）
BAS| 年初（business year start，仅含工作日）

另外，你可以在频率代码后面加三位月份缩写字母来改变季、年频率的开始时间。
* Q-JAN、BQ-FEB、QS-MAR、BQS-APR 等。
* A-JAN、BA-FEB、AS-MAR、BAS-APR 等。

同理，也可以在后面加三位星期缩写字母来改变一周的开始时间。
* W-SUN、W-MON、W-TUE、W-WED 等。

在这些代码的基础上，还可以将频率组合起来创建的新的周期。例如，
可以用小时（H）和分钟（T）的组合来实现 2 小时 30 分钟：


```python
pd.timedelta_range(0, periods=9, freq="2H30T")
```




    TimedeltaIndex(['00:00:00', '02:30:00', '05:00:00', '07:30:00', '10:00:00',
                    '12:30:00', '15:00:00', '17:30:00', '20:00:00'],
                   dtype='timedelta64[ns]', freq='150T')



所有这些频率代码都对应 Pandas 时间序列的偏移量，具体内容可以在
pd.tseries.offsets 模块中找到。例如，可以用下面的方法直接创建
一个工作日偏移序列：


```python
from pandas.tseries.offsets import BDay
pd.date_range('2015-07-01', periods=5, freq=BDay())
```




    DatetimeIndex(['2015-07-01', '2015-07-02', '2015-07-03', '2015-07-06',
                   '2015-07-07'],
                  dtype='datetime64[ns]', freq='B')



### 时间迁移
另一种常用的时间序列操作是对数据按时间进行迁移。Pandas 有两种解决这类问题的方法：shift() 和 tshift()。简单来说，shift() 就是迁移数据，而 tshift() 就是迁移索引。两种方法都是按照频率代码进行迁移。下面我们将用 shift() 和 tshift() 这两种方法让数据迁移 900天


```python
fig, ax = plt.subplots(3, sharey=True)
fig.subplots_adjust(hspace=0.4, wspace=0.4)
# 对数据应用时间频率，用向后填充解决缺失值
stock = stock.asfreq('D', method='pad')
stock.plot(ax=ax[0])
stock.shift(900).plot(ax=ax[1])
stock.tshift(900).plot(ax=ax[2])

# 设置图例与标签
local_max = pd.to_datetime('2008-01-02')
offset = pd.Timedelta(900, 'D')
ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')
ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[4].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')
ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[2].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');
```

#### 练习

1. 计算股票的日收益率？
2. 计算股票一年期的投资回报率

### 练习
画出股票代码为603970.SH的股票，在2020年05月18日5分钟均值走势图。




```python

```
