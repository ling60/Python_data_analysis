# Python环境变量设置及第三方包的安装介绍

本文档主要讲解该如何在不同的操作系统里，安装Python的第三方包。

### 仅安装了Python的安装第三方包的方法

a. 在Windows开始菜单旁，搜索cmd

b. 点击 命令提示符，然后输入pip

![image-20200220154710156](C:\Users\ling\AppData\Roaming\Typora\typora-user-images\image-20200220154710156.png)

如果没有出现图片上的内容，应该是Python的路径没有设置好。可参考https://www.runoob.com/python/python-install.html 修改环境变量，或进入到Python目录下再输入 pip

c. 安装某个package的命令为

pip install pcknm(包的名字)，如果pip无法正常运行，请按照上面关于环境变量设置的说明，在环境变量中添加pip路径。

比如，安装 jieba就用:

    pip install jieba



### Anaconda安装第三方包的方法


默认环境下，anaconda 已经内置了200+的packages，大家可以通过window开始菜单点击anaconda navigator 查看里面都安装了哪些packages（包）

   ![img](file:///C:\Users\ling\Documents\Tencent Files\7215494\Image\Group2\T}\2S\T}2S3_SHC066OJCDZP{4@]P.jpg)

如果需要的package不在里面，则点击 anaconda prompt，然后在里面输入 conda install pkgnm（包名），如果conda 上面没有找到包，那么可以用上面的 pip来安装