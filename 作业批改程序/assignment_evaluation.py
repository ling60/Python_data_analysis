import zipfile
import os
import CheckDuplicate
import pandas as pd
# import subprocess  #for run other python script
# import pycode_similar  #另外一个可能的判断代码相似度的包

"""
* 下载当期作业，并解压到一个文件夹下。即，该文件下有N个zip文件，每个zip文件对应一个学生的作业
*	首先运行 ‘extract_to_one_folder’, 用处为将每个单独的zip文件解压，并将其中的代码文件（.pu, .ipynb）复制到py_files下。默认py_files在zip文件夹中，即与所有单独的zip文件同一目录下。
调用此函数需要给出参数or_file_folder，即zip文件夹。函数运行会print出未复制代码的文件，通常意味着该文件中没有找到py或ipynb文件。可在超星中退回该学生作业，原因写明需要提交代码文件。
*	evaluate_code为正式批改程序， 该函数会首先print出学生提交的代码，然后询问是否运行，此过程中请注意代码是否有重大问题，比如进入死循环，或代码插入（此情况不多见）。如果有，输入n，其他输入，y或回车等均会运行代码。
函数调用过程中，遇到报错的情况程序会直接给出60分。其他正常程序会先print程序，再询问是否运行，而后提示给出分数，及评语，分数和评语都可以不给（直接回车即可）。
程序运行完成后，会返回marks df，同时会在本地生成一个marks_file.csv文件。建议重新查看一下报错的学生代码以防有误。
相关参数：
第一次调用函数，可以将参数run_all_files=False改为True，程序会自动生成一个全新的mark_file.csv成绩文档。后面多次调用时，可以用默认的False，程序会打开已有mark_file.csv，并在其后添加成绩。
Run_files参数是用来跑个别代码的，具体见参数说明，通常用默认值即可。
*	CheckDuplicate用来查重。前几周运行下看看即可。 CheckDuplicate.isDuplicate是主函数，参数path是python源码集所在路径。 MIN_COS_DIST用于更改cosine距离阈值，范围(0, 1), 默认0.9。
"""


def extract_to_one_folder(ori_file_folder, py_files='py_files', create_marks_file=True, mark_file=None):
    """
    此函数主要功能为：把所有超星每个学生的代码从对应的zip包中解压，在文件名中加上学号，并保存到同一个文件夹。
    程序运行结束会print没有copy成功的学号
    :param create_marks_file: 是否要创建一个新的marks文档。默认为True
    :param mark_file: 如果create_marks_file为False，则此参数为已有的marks文档
    :param ori_file_folder: 所有原始zip文件所在目录。
    :param py_files: 代码文件目标目录,即代码.py/.ipynb文件均会在解压后复制到此文件夹中。这个文件夹会出现在ori_file_folder内。
                    程序会在文件夹不存在时自动创建

    """

    # 判断py_files文件夹是否存在，不存在则创建
    if not os.path.exists(os.path.join(ori_file_folder, py_files)):
        os.mkdir(os.path.join(ori_file_folder, py_files))
        print('py_files created in {}'.format(ori_file_folder))

    # 得到所有zip文件的文件名
    zipfiles = [f for f in os.listdir(ori_file_folder) if f.endswith('.zip')]
    stu_ids = [sid.split('-')[0] for sid in zipfiles]  # 默认学号为文件名以-分隔后0位置字符串
    print('In total, there are {} zip files and {} student ids'.format(len(zipfiles), len(set(stu_ids))))
    copied = []
    for zfile in zipfiles:
        with zipfile.ZipFile(os.path.join(ori_file_folder, zfile), mode="r") as toExtrat:
            # 得到学号，超星下载文件名格式为：“学号-姓名.zip”
            stu_id = zfile.split('-')[0]
            for file in toExtrat.namelist():
                if file.endswith(".py") or file.endswith(".ipynb"):
                    # 将py文件名前面增加学号，并保存到py_files文件夹里,命名为 42XXXXXX-实际作业命名
                    toExtrat.getinfo(file).filename = os.path.join(
                        ori_file_folder, py_files, stu_id+'-'+file)
                    toExtrat.extract(file)
                    # 记录已解压并复制的学号
                    copied.append(stu_id)

    if copied:
        print('Py files copied except', [stu for stu in stu_ids if stu not in copied])
    else:
        print('all files are copied')

    # 生成成绩文件
    if create_marks_file:
        marks = pd.DataFrame(columns=['stu_id', 'mark', 'comment'])
        marks['stu_id'] = list(set(stu_ids))
        marks.to_csv(mark_file, index=False, encoding='utf8')
        print('Mark file created in {} as {}'.format(os.getcwd(), mark_file))


def check_code_similarity(py_files):
    """
    查重。需要把CheckDuplicate.py与当前代码放在同一个文件夹下。
    :param py_files: 保存.py文件的文件夹
    :return:
    """
    duplicate_set = CheckDuplicate.isDuplicate(py_files)
    print(duplicate_set)


def evaluate_code(py_files, mark_file, run_all_files=False, run_files=False):
    """
    运行py_files下所有.py文件。

    另外一种可能的方式是：

    subprocess.run(["python", "script1.py"])

    :param run_files: 可给定一个list用以单独运行一些代码
    :param run_all_files: 是否运行所有作业代码？是的话，会将原有marks.csv清空
    :param mark_file: 成绩结果csv
    :param py_files: 存放所有python代码文件的文件夹

    """
    marks = pd.read_csv(mark_file, dtype={'stu_id': str})
    print('current marks\n', marks)
    # 如果确定运行所有代码，则重新创建marks文档
    if run_all_files:
        stuid_torun = marks.stu_id.values

    # 仅运行一部分给定的作业代码，调用函数时需要给出run_files具体list里面是代码文件名
    elif run_files:
        stuid_torun = run_files
    # 如果未选择运行所有代码，则只运行目前没给成绩的
    else:
        # 读取已有成绩文档，并删除未给成绩的记录
        # 删除掉成绩为空，即此前没给分数的学生记录
        stuid_torun = marks[marks.mark.isnull()].values

    # 确定要运行的文件
    files_to_run = [f for f in os.listdir(py_files) if f.endswith('.py') and f.split('-')[0] in stuid_torun]
    print('{} files will be running'.format(len(files_to_run)))

    # 准备运行学生代码
    input('回车开始运行代码。。。')
    for pfile in files_to_run:
        stu_id = pfile.split('-')[0]
        print(stu_id)
        if marks.loc[marks['stu_id'] == stu_id, 'mark'].notnull().any():
            remark = input('这个学生成绩已给出{}，是否重新打分？是（y），否（n）'.format(marks.loc[marks['stu_id'] == stu_id, 'mark'].item))
            if remark == 'n':
                continue
            else:
                marks.drop(marks[marks.stu_id == stu_id].index, inplace=True)

        print('Trying to run', stu_id, 'assignment, named ', pfile)

        # 打开学生代码文件，并print
        with open(os.path.join(py_files, pfile), "r", encoding='utf-8') as ff:
            code = ff.read()
        print(code)  # 将代码print出来

        # 根据代码判断是否需要运行
        runCode = input(
            '是否运行该代码? 终止程序：请输入"quit", 无需运行，请输入n。 运行代码：直接回车或所有其他输入: ')

        if runCode == 'quit':
            break
        elif runCode == 'n':
            continue
        else:
            try:
                exec(code, globals())
                # 根据代码给出分数
                mark = input('请给出该作业分数：')

                if mark != str(100):
                    # 如有需要给出评语
                    comment = input('评语（可不写，直接回车）')
                else:
                    comment = None

                # 将成绩加入csv
                marks.loc[marks['stu_id'] == stu_id, ['mark', 'comment']] = [float(mark), comment]
                print('mark saved for ', stu_id, mark, comment)
            # 如果运行程序报错，自动给60分
            except Exception as e:
                print(e)
                marks.loc[marks['stu_id'] == stu_id, ['mark', 'comment']] = [60, '代码报错']
                print('mark saved for ', stu_id, 60, '代码报错')
                input('是否开始下一位同学的代码？')

    if marks[marks.duplicated(['stu_id'])] is True:
        print('以下学生成绩有重复情况，需要注意')
        print(marks[marks.duplicated(['stu_id'])])
    # print(marks)

    marks.to_csv(mark_file, index=False, encoding='utf8')
    return marks


# 可以直接修改变量
ori_file_folder = r'Week3'
py_files = os.path.join(ori_file_folder, 'py_files')
# 在当前代码文件夹下建立对应的marks文档
mark_csv = os.path.join(ori_file_folder+'_marks.csv')
# 第一步，解压并复制全部py文件到一个文件夹
# extract_to_one_folder(ori_file_folder, py_files='py_files', create_marks_file=True, mark_file=mark_csv)
# # 第二步，查重
# check_code_similarity(py_files)
# # 第三步，批改作业
evaluate_code(py_files, mark_file=mark_csv)