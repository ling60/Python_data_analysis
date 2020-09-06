# Jupyter Notebook安装、启动、使用教程



本文主要给大家介绍Jupyter notebook的安装、启动和使用。Jupyter Notebook是一个常见的Python IDE，同时兼具Markdown（文本编辑）及code（代码编写）的功能，非常适合初学者使用。**notebook文件的后缀名（扩展名）是 .ipynb**



## 安装

依据你的Python配置环境：

1. 如果你的Python环境是以Anaconda为基础的，那么无需额外按照notebook，因为已经被集成进anaconda里面了

2. 如果你只按照了Python，那么（详细安装说明请见（https://jupyter.org/install）），具体方法如下：

   a. 在Windows开始菜单旁，搜索cmd

   ![image-20200220154626057](pics\image-20200220154626057.png)

   b. 点击 命令提示符，然后输入pip

   ![image-20200220154710156](pics\image-20200220154710156.png)

如果没有出现图片上的内容，应该是Python的路径没有设置好。可参考https://www.runoob.com/python/python-install.html 修改环境变量，或进入到Python目录下再输入 pip

c. 安装某个package的命令为

pip install pcknm(包的名字)，如果pip无法正常运行，请按照上面关于环境变量设置的说明，在环境变量中添加pip路径。

比如，安装 notebook就用:

```Python
pip install notebook
```

## 启动

同样，依据你的Python环境有两种启动notebook的形式

1. 在anaconda环境下，请在windows开始菜单，点击Anaconda Navigator，而后在弹出界面点击Jupyter Notebook 即可
2. 在Python环境下，请在CMD下，直接输入 jupyter notebook，如果显示不是内部命令，说明Python环境变量没有设置好，请参考https://www.runoob.com/python/python-install.html 修改环境变量。

**notebook正常运行后**，你可以在浏览器（对，就是你上网用的那个浏览器）看到类似下方的页面：

![image-20200301144905217](pics\image-20200301144905217.png)



这个页面就是notebook在你的系统里建立一个小小的服务器，与此同时，你的系统里应该还会看到一个类似下面图片的黑色小框框窗口：

![image-20200301145036771](pics\image-20200301145036771.png)

**请一定注意，从你开始运行notebook到写程序，运行完毕之前，请一定一定不要关闭这个窗口，如果关闭了就会出现程序无法正常运行的情况。**

## 使用

### 打开/新建一个notebook
![image-20200301150306050](pics\image-20200301150306050.png)

   a. 新建一个notebook文件：点击3区内New 按钮
   b. 上传一个notebook文件，点击3区内upload按钮, upload之后，上传的notebook会出现在左边的文件列表里，点击文件名字即可打开（会出现一个新的页面）
   c. 图片中1区为目录下的文件夹，2区为目录下的文件内容

### 一个正常的notebook文件（文件扩展名为.ipynb）如下：

   ![image-20200301153801848](pics\image-20200301153801848.png)

每一个notebook页面，都是由多个单元格（cell）组成的。上图页面中共5个单元格。每个单元格有两种不同的属性，一种是Markdown 即文本形式（单元格1，2, 5），另外一种是code即编程形式（单元格3，4）。我们可以通过菜单下方toolbar右侧，蓝色框框里看到当期cell的属性，以及对其属性做更改，或者也可以采用快捷键（m/y来分别代表markdown和code）.

### Markdown Cell介绍

Markdown指代简易标记文本文档，意思是用一些特殊符号来代表一定的格式。比如，# 代表标题，一个 # 是最高级标题，## 就是二级标题，以此类推。相关的标记规则，可以参考https://help.github.com/articles/markdown-basics/ 或在notebook页面，点击help菜单，再点击 markdown

### Code Cell介绍

Code就是指编程模式了，这部分与iPython相结合的编程交互界面。因此，主要用法与iPython相同，我们可以采用TAB键获得可能的代码，方法。在代码后面加“？”来显示帮助文档等等。

需要注意的问题有：

1. 每次运行一个单元格后，左侧 In【】中会显示一个数字，这个数字代表着程序运行的顺序，数字越小说明程序运行得越早，在后面运行的程序有可能是的前面运行过的结果发生改变。
2. 一个单元格内，一般只有最后一行的代码可以不需要print直接把结果显示出来。比如，下图只会显示最后一行5+6的结果，上面两行的结果并不显示。因此如果需要看到结果，则需要添加print
![image-20200301160217151](pics\image-20200301160217151.png)

### 常见问题

1. 为什么我的程序正常，却运行不出结果？

   如果你的程序正常，但是没有显示任何结果，请查看是否在cell左边的 In[] 里面有一个 * 号，如下图所示

![image-20200301160435029](pics\image-20200301160435029.png)

这就意味着你可能把notebook的服务器关掉了（就是启动notebook之后会出现的黑色命令行框框）。这种情况下，请重新启动notebook。在未完成编程以及notebook使用之前，请一定要不关掉命令行对话框。

2. notebook有哪些快捷键和使用技巧？

   请参考菜单栏，help（帮助）查看相关内容

3. 为什么我的变量的值变了？

   大概率是因为你不小心重新赋值了这个变量。在notebook中，程序的运行不按照传统的从上往下运行的顺序，而是依据每个单元格运行的次序而定。比如，下图中，一共三个cell，最上面的最先运行（左侧In中有数字1），最下面的第二次运行（左侧显示2），这时，如果我们在两个cell中插入一个cell，并且要求程序显示a的值，即便该cell在两次运行中间，相当于在 a = 6 之后，但在 a=8 之前，程序依然会按照运行次序，返回结果8，而不是6.

   ![image-20200301161004874](pics\image-20200301161004874.png)

Happy Coding!