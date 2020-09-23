# Anaconda下Python环境下载及安装



## Anaconda介绍

[Anaconda](https://www.anaconda.com/products/individual) 是一个集成了几千个Python第三方包的一个Python环境。推荐以数据分析为目的学习Python的同学直接下载安装这个环境。省去很多第三方包的安装和配置过程。

如果你只想安装Python,而后逐个单独下载和安装每个package，请参考[Python独立安装下载介绍](Python_install_setup.md)

## 下载地址

以下提供两个下载地址，一个是官网地址，一个是清华镜像。在国内的同学建议直接查看清华镜像部分即可。

### 官方下载网址：

https://www.anaconda.com/distribution/

### [清华镜像](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)，国内网，速度较快 （国内下载推荐）

Anaconda安装包下载链接：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

根据你自己的操作系统版本，挑选一个下载。最下面的一个是64位的windows，这个可能是大部分同学的选择。

![清华镜像Anaconda下载页面](pics\anaconda_tsinghua_list.png)

### Anaconda安装

以下几个页面需要注意：

1. 如果是安装在自己电脑上，尽量选择为所有用户安装

![Anaconda安装用户选择](pics\anaconda_instal_1.png)

2. 安装路径选择如果需要修改，请一定记清相关路径，如果可以，尽量不改

![Anaconda安装路径选择](pics\anaconda_instal_2.png)

3. 其他页面点击 Next 即可

### 用anaconda安装新的package

默认环境下，anaconda 已经内置了2000+的packages，大家可以通过window开始菜单点击anaconda navigator 查看里面都安装了哪些packages（包）

![Anaconda Start Up Menu](pics\anaconda_startup_menu.png)

如果需要的package不在里面，则点击 anaconda prompt，然后在里面输入 conda install pkgnm（包名），如果conda 上面没有找到包，那么可以 pip来安装