# Lecture 5: Python function and File RW

本次课程主要介绍Python语言中的函数和文件读取相关内容。

## 函数Function

函数是一组“完整”的用以完成一个特定任务的程序代码。是编程语言中非常重要的一个组成部分，也是一个对程序进行抽象和重用的过程。函数可以看作是一些代码的集合, 或者是子程序。

当一个函数被“定义”之后，任何人都可以根据函数的参数和返回值来“调用”函数。其中，参数指在调用函数时提供的对应的变量的值，返回值则代表函数运行结束之后，返回的变量值。换句话说，参数是函数“输入”的部分，而，返回值是函数“输出”的内容。

在Python中，len(),float(), str.split()都是函数。而在括号中我们写入的内容对应的就是函数的参数。


```python
# 示例： 定义一个函数

# def 为定义函数的关键词，sayhello为自己取的函数的名字，“（）”里面代表着参数，即便没有参数也必须要有括号
# name为自定义的参数名
def sayhello(name):
    # 此函数的唯一作用是print用户给出的name对应的值
    print('hello, ', name)
```


```python
# 示例：调用上面的函数
sayhello('Jack')
```

    hello,  Jack
    

### 函数输入部分：参数

函数的参数可以有0-多个。每个参数之间以“,”分隔。参数名自取。

参数可以看作是函数的输入部分，调用函数的时候我们把需要改变的值放置到参数的位置。比如，如果一个函数的目的是求给定值的平方，那么这个“给定值”就是我们函数的参数。

参数有以下几种：

- required argument
- default argument
- keyword argument
- variable-length argument

具体介绍参见：https://www.tutorialspoint.com/python3/python_functions.htm
![image.png]

### 函数的处理过程

函数，也就是def下属的代码块都从属于函数本身的内容。需要注意的是，无论是参数，还是在函数中额外定义的变量都只作用在函数范围内，我们通常称之为**局部变量**。而函数外定义的变量则对应称之为**全局变量**


```python
x = 99 # 全局变量

def func(x):
    y = x + 88 # 局部变量
    return y

print(x) # 在函数外可以调用全局变量
print(y) # 在函数外不能调用函数内的局部变量
```

    99
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-3b5a87ce058a> in <module>
          6 
          7 print(x)
    ----> 8 print(y)
    

    NameError: name 'y' is not defined



```python
# 局部变量的值不会改变全局变量的值 (字符串不可变)

def try_to_change(n):
    n = 'Mr. Wang'
    return n

name = 'Mrs Liu'
name1 = try_to_change(name)
print(name)
print(name1)
```

    Mrs Liu
    Mr. Wang
    

**尽量不要将函数内外的变量名混用，即不要用一个变量名定义多个变量!**

### 函数的输出部分：返回值

每个函数都有返回值（return），当没有定义return的时候，默认:

```
return = None
```


**练习**

写一个函数用以计算一个人的BMI值（体重（公斤）除以身高（米）平方）。

## 文件读写

在操作系统内，每个文件都有以下几个属性：

1. 文件名字及后缀名
2. 文件路径，既文件所在位置

比如，lecture5.pptx的文件名为"lecture5.pptx"其中，.pptx是其后缀名，代表文件的类习性。
当我们选中文件点击右键，可以看到文件的位置、类型等相关信息。


### 文件类型

通常我们将文件分为两类：
1. 纯文本文件，plaintext files
2. 二进制文档, binary files

纯文本文档的意思是：

> A text file (sometimes spelled "textfile"; an old alternative name is "flatfile") is a kind of computer file that is structured as a sequence of lines of electronic text. A text file exists stored as data within a computer file system. 

当用记事本打开二进制文档的时候，里面显示的都是乱码


### 文件所在位置

如上所述，通过一些方法我们可以查明文件的位置。当这个位置带有盘符，如C:\,D:\的时候，代表是绝对路径。

但在写程序的时候我们常采用"相对路径"。相对是指“文件”相对于我们的“代码运行环境”而言的相对位置。

在编程语言中，这个“代码运行环境”叫做，current working directory，当前工作路径


```python
# 可以通过调用os包获取当前工作路径
import os
os.getcwd()
```

### Python 读写文件的方法

请尽量使用下面的方法来打开文件


```python
with open('data/test.txt') as ff: # 打开data目录下的test.txt文档，并将"该文件"起名为ff
    testfile = ff.read() # 读取文档里面的全部内容，并赋值给testfile这个变量
print(testfile)
```

请注意，ff为一个文件流的概念，read方法后面没有传递任何参数的时候，代表一次性读取所有内容。此外，我们可以传递数字以代表读取几个“字”,每读取完这几个字之后，文件流就会将读取过的内容“删除”，因此再继续读取的时候，将从之前读过的内容之后进行读取。而不是从头开始
