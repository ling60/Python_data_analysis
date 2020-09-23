# Python环境下载及安装

## Python单独安装

官方网站直接下载：https://www.python.org/downloads/

## 第三方包下载及安装

a. 在Windows开始菜单旁，搜索cmd

b. 点击 命令提示符，然后输入pip

![image-20200220154710156](C:\Users\ling\AppData\Roaming\Typora\typora-user-images\image-20200220154710156.png)

如果没有出现图片上的内容，应该是Python的路径没有设置好。可参考https://www.runoob.com/python/python-install.html 修改环境变量，或进入到Python目录下再输入 pip

c. 安装某个package的命令为

pip install pcknm(包的名字)，如果pip无法正常运行，请按照上面关于环境变量设置的说明，在环境变量中添加pip路径。

比如，安装 jieba就用:

    pip install jieba
