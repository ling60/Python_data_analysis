# Lecture 2: Introduction to Python Data Structure

This is a Jupyter notebook for Python for Data Analysis course.


## Part 0, Introudction to Jupyter Notebook
This course notes is presented as an IPython Notebook, which has been renamed to Jupyter Notebook.

Jupyter Notebook是以一段段代码/文字块的组合而显示的。Notebook有两种基本形式：Commond Mode and Edit Mode. Edit Mode可以看到光标，Commond Mode则看不到，两个mode下快捷键不同。通常，Commond Mode用于对notebook的整体进行修改，如在下方增加一个代码块（b），或将代码块改为代码或文字块（m）

* 可以点击上方菜单，help-->User interface tour对notebook有个全面的了解
* 需要运行代码，请按 shift-enter, 最后一行代码的结果会在下方显示出来
* 在commond mode下按 h 会显示快捷键列表
* IPython notebooks documentation: <https://ipython.org/ipython-doc/3/notebook/notebook.html#introduction> (old version).
    * New version, but less informative. <https://jupyter.readthedocs.io/en/latest/content-quickstart.html>
* You can search for more notes here: <https://nbviewer.jupyter.org/>



```python
#press 'b' in commond mode (where the border of the cell is in blue color)
```

## Part 1, Introduction to Python



**Exercise**
请在下方新建一个代码块，写出并运行代码，让电脑打印出，“Hello Python”

**Exercise**

Assign each of the following to a variable?
* 4
* 3.1415
* 1.0
* 2+4j
* 'Hello'
* 'World'

哪些可以做加减乘除?


```python
#
```


```python
# 观察下面两个cell显示结果的差异
print(2+3)
```


```python
2+3
```


```python
# 输入代码查看上面练习中各个变量的类型

```

## Part 2, import modules and packages

The following codes show how to import and use modules and packages


```python
import math
print(math.pi)
print(math.e)
```

安装新的package时，请在cmd/terminal下（非python环境内），输入代码：

```
pip install pkg
```

pkg, 代表需要安装的package 的名字。**请不要在notebook里运行这些代码**

如果已经安装了Conda环境，可以用下面的命令查找是否一个package已经安装好了，比如，想看本地是否存在pandas这个package:

```
conda list pandas
```

如果想在conda环境下安装package，除了pip之外，还可以采用以下代码：

```
conda install pkg
```

想了解一个package的相关信息


```python
dir(math)
```

## Part 3. The interesting string

To know more of string, take a look at: <https://docs.python.org/3.7/library/stdtypes.html#string-methods>




**Exercise**

Learn how to slice and index a string. Try to understand the concept by doing the exercises.


```python
ss = 'this is fun'
ss[1]
ss[:7]
```

**Exercise Four**

Be familiar with common string related methods.

```
ex.capitalize()
ex.count('Python')
ex.find('py')
ex.lower()
ex.split()
```


```python
ex = 'I think Python is an interesting and useful language for numerical computing!'
```

**Exercise Five**

如何获取下列字符：
* 'hello'
* 'University'


```python
s1 = 'welcome to our university'
s2 = 'hello!'
```


```python

# to get University, we will first locate 'university' location 
# and then use it to get the word, and finally capitalize the word

```

下面两行代码会得到什么结果？
```
s1 + s2
s2*3
```


```python

```

**Exercise**

写代码完成下列练习：
1. 查找在s1中是否有‘hello’
2. 获取s1的前6个字符
3. 从s2中获取'hlo'


```python

```

**Exercise**

从ex变量里得到：

* '!'
* '!gnitupmoc laciremun rof egaugnal lufesu dna gnitseretni na si nohtyP’ (所有字母顺序反过来)
* 'gnitupmoc'	(computing顺序反过来)


```python

```

**Exercise**

```
ex = 'I think Python is an interesting and useful language for numerical computing!'
```
ex 字符串中，一共有几个词？在英文中怎么定义词？如何把上述字符串分成一个个的词？这些词该如何存为一个变量？



```python
# Tips: split
```

## Part 4. Control Flow

程序控制（控制流程）
- 控制是否每一行代码都会运行
    - 判断
- 以及运行次数
    - 循环


```python

```


### Python 的缩进（indentation）

- Python依靠"文字缩进"级别来判定函数,代码语句的归属问题
- 同一级别的语句要对齐，不能有空格或缩进
- 不同的缩进级别代表着代码间的级别
- 缩进通常是4个空格或者直接按tab键

### 判断

python判断部分与其他语言基本一致，主要的形式如下：
```
if condition(is True):
    code block 1
elif condition(is True):
    code block 2
else:
    code block 3
```


```python
# 请注意两行print语句前的缩进部分
x = 10
y = 20
if x > y:
    print(x)
else:
    print(y)
```

### While loops

Python 的while循环与其他语言相似，通常用来做需要在程序运行过程满足条件后再停止循环的内容，换句话说，while循环不一定能知道程序最终会循环多少次，也就意味着，有可能造成死循环


```python
n = 5
while n > 0:
    print(n)
    n = n-1
print('the end')
```

### For loops

Python的for循环是与其他编程语言差距较大的一个地方。

for循环，也叫做遍历，意思是将一个可以“遍历”的数据类型中的每一个元素一一“取出”，而后进行相应的“处理”。

python将这个过程大大简化了。Python是可以用任意一个名字（可以看成是临时变量名）来**直接遍历一个变量里面的各个元素**，而每次遍历将按顺序直接返回该变量中的每一个元素。


```python
a_word = 'hello'
# item可以改成任意一个自定义的变量名
for letter in a_word:
    print(letter)
```

#### 其他语言for语句与python的差别

for循环代表着指定循环的次数，最常见的情况是循环一个string，然后获取里面的每一个位置的字符是什么。

其他的编程语言的逻辑通常是先判断字符串的长度，然后按照index，从0开始遍历，之后
```
a_word = 'hello'
count = 0
```
从0开始遍历，用count做index取值，同时对count加1，一直到count等于a_word的长度，也就是变量的结尾。

**练习**

如何用a_word的index去遍历？


```python

```


```python

```
