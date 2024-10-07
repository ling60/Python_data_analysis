# 如何修改Jupyter Notebook的启动文件夹

如果你的电脑已经将Python及Anaconda的加到了环境变量里面，那么可以在Windows的文件浏览器的地址栏直接输入 jupyter notebook 。

![在文件浏览器直接打开jupyter](pics\open_jupyter_in_explorer.png)

此外可以通过如下说明修改默认启动文件夹：

1. 首先进入cmd，如果Python环境变量已经设置成功可以直接在系统打开cmd。如果没有设置环境变量，可以从开始菜单anaconda下选择进入，如下图所示：

![进入cmd](pics\open_anaconda_prompt.jpg)

2. 在cmd下，输入 *jupyter notebook --generate-config*
   
   ![生成config文件](pics\jupyter_generate_config.png)

   请注意涂黑部分应该是你自己电脑的用户名

3. 打开对应路径下的对应文件（应该是C盘用户（user）-你的用户名 这个文件夹下 jupyter_notebook_config.py），搜索 “c.NotebookApp.notebook_dir”, 版本不同也可能是 “c.ServerApp.root_dir”，请注意画线部分上面的注释应该是 “The directory to use for notebooks and kernels.”
   
   ![打开config文件](pics\Search_for_key_string.png)

4. 取消该行注释（删掉最前方的#），在等号后面的引号中输入新的文件夹路径

   ![修改文件夹](pics\change_folder.png)

5. 关闭所有应用，重启电脑路径应该就修改好了