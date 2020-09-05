# Python环境下载及安装

### 可以参考后面的网址，进行安装 https://www.runoob.com/python/python-install.html ###

或参考后面的内容

### （2个选择）

1. Anaconda

我们推荐直接下载Anaconda，这是一个 集合了Python程序以及200+Python第三方package的应用包，如果后期使用Python较多，可以尽量安装这个。

Anaconda 下载及安装（如果连外网比较快的话，建议去官网，因为官网能够直接根据你的系统选择你需要下载的安装包）：

- 官方下载网址：

https://www.anaconda.com/distribution/

- 清华镜像，国内网，速度较快

https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=A 

把页面拉倒最下面


![img](file:///C:\Users\ling\AppData\Roaming\Tencent\Users\7215494\QQ\WinTemp\RichOle\1629{6X]B5[PJET[JPSNNTJ.png)

根据你自己的操作系统版本，挑选一个下载。最下面的一个是64位的windows，这个可能是大部分同学的选择。

2. Anaconda安装，按照提示一步步点下去就可以

3. Python单独安装

   官方网站直接下载：https://www.python.org/downloads/

   **仅安装了Python的同学，请再安装一下jupyter notebook。** 详细安装说明请见（https://jupyter.org/install）
   
   具体方法如下：
   
   a. 在Windows开始菜单旁，搜索cmd
   
   ![image-20200220154626057](C:\Users\ling\AppData\Roaming\Typora\typora-user-images\image-20200220154626057.png)
   
   b. 点击 命令提示符，然后输入pip
   
   ![image-20200220154710156](C:\Users\ling\AppData\Roaming\Typora\typora-user-images\image-20200220154710156.png)

如果没有出现图片上的内容，应该是Python的路径没有设置好。可参考https://www.runoob.com/python/python-install.html 或进入到Python目录下再输入 pip

c. 安装某个package的命令为

pip install pcknm(包的名字)，如果pip无法正常运行，请按照上面关于环境变量设置的说明，在环境变量中添加pip路径。

比如，安装 notebook就用:

```Python
pip install notebook
```



本课程额外安装notebook应该就够用了，如果有需要后期可以再装

#### 用anaconda安装新的package

默认环境下，anaconda 已经内置了200+的packages，大家可以通过window开始菜单点击anaconda navigator 查看里面都安装了哪些packages（包）

   ![img](file:///C:\Users\ling\Documents\Tencent Files\7215494\Image\Group2\T}\2S\T}2S3_SHC066OJCDZP{4@]P.jpg)

如果需要的package不在里面，则点击 anaconda prompt，然后在里面输入 conda install pkgnm（包名），如果conda 上面没有找到包，那么可以用上面的 pip来安装