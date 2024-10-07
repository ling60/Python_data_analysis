import zipfile
import os
import CheckDuplicate
import pandas as pd
# import subprocess  #for run other python script
# import pycode_similar  #另外一个可能的判断代码相似度的包


# 下载当期作业，并解压到一个文件夹下。即，该文件下有N个zip文件，每个zip文件对应一个学生的作业


def extract_to_one_folder(ori_file_folder, py_files='py_files'):
    """
    此函数主要功能为：把所有超星每个学生的代码从对应的zip包中解压，在文件名中加上学号，并保存到同一个文件夹。
    程序运行结束会print没有copy成功的学号
    :param ori_file_folder: 所有原始zip文件所在目录。
    :param py_files: 代码文件目标目录,即代码.py/.ipynb文件均会在解压后复制到此文件夹中。这个文件夹会出现在ori_file_folder内。
                    程序会在文件夹不存在时自动创建

    """

    if not os.path.exists(os.path.join(ori_file_folder, py_files)): # 判断py_files文件夹是否存在，不存在则创建
        os.mkdir(os.path.join(ori_file_folder, py_files))
        print('py_files created in {}'.format(ori_file_folder))

    # 得到所有zip文件的文件名
    zipfiles = [f for f in os.listdir(ori_file_folder) if f.endswith('.zip')]
    stu_ids = [sid.split('-')[0] for sid in zipfiles]
    copied = []
    for zfile in zipfiles:
        with zipfile.ZipFile(os.path.join(ori_file_folder, zfile), mode="r") as toExtrat:
            # 得到学号，超星下载文件名格式为：“学号-姓名.zip”
            stu_id = zfile.split('-')[0]
            for file in toExtrat.namelist():
                if file.endswith(".py") or file.endswith(".ipynb"):
                    # 将py文件名前面增加学号，并保存到py_files文件夹里,命名为 42XXXXXX-实际作业命名
                    toExtrat.getinfo(file).filename = os.path.join(ori_file_folder, py_files, stu_id+'-'+file)
                    toExtrat.extract(file)
                    # 记录已解压并复制的学号
                    copied.append(stu_id)

    print('Py files copied except', [stu for stu in stu_ids if stu not in copied])


def check_code_similarity(py_files):
    """
    查重。需要把CheckDuplicate.py与当前代码放在同一个文件夹下。
    :param py_files: 保存.py文件的文件夹
    :return:
    """
    duplicate_set = CheckDuplicate.isDuplicate(py_files)
    print(duplicate_set)


def evaluate_code(py_files, mark_file='mark_file.csv', run_all_files=False, run_files=False):
    """
    运行py_files下所有.py文件。

    另外一种可能的方式是：

    subprocess.run(["python", "script1.py"])

    :param run_files: 可给定一个list用以单独运行一些代码
    :param run_all_files: 是否冲头运行所有代码？是的话，会将原有marks.csv清空
    :param mark_file: 成绩结果csv
    :param py_files: 存放所有python代码文件的文件夹

    """

    # 如果确定运行所有代码，则重新创建marks文档
    if run_all_files:
        files_to_run = [f for f in os.listdir(py_files) if f.endswith('.py')]
        marks = pd.DataFrame(columns=['stu_id', 'mark', 'comment'])
    # 仅运行一部分给定的作业代码，调用函数时需要给出run_files具体list里面是代码文件名
    elif run_files:
        files_to_run = run_files
        marks = pd.read_csv(os.path.join(py_files, mark_file), dtype={'stu_id': str})
    # 如果未选择运行所有代码，则只运行目前没给成绩的
    else:
        # 读取已有成绩文档，并删除未给成绩的记录
        # if os.path.exists(os.path.join(py_files, mark_file)):
        marks = pd.read_csv(os.path.join(py_files, mark_file), dtype={'stu_id': str})
        # 删除掉成绩为空，即此前没给分数的学生记录
        marks.dropna(subset=['mark'], inplace=True)
        files_to_run = [f for f in os.listdir(py_files) if (f.endswith('.py') and f.split('-')[0] not in marks.stu_id.values)]

    print('{} files will be running, {}'.format(len(files_to_run), files_to_run))
    input('Enter to continue')

    for pfile in files_to_run:

        stu_id = pfile.split('-')[0]
        if stu_id in marks.stu_id.values:
            remark = input('这个学生成绩已给出，是否重新打分？是（y），否（n）')
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
        runCode = input('是否运行该代码? 是：直接回车。 否，请输入n。 （所有非n输入都会运行代码）: ')

        if runCode != 'n':
            try:
                exec(code, globals())

                # 根据代码给出分数
                mark = input('请给出该作业分数：')

                # 如有需要给出评语
                comment = input('评语（可不写，直接回车）')

                # 将成绩加入csv
                marks = marks.append({'stu_id': stu_id, 'mark': mark, 'comment': comment}, ignore_index=True)
                print('mark saved for ', stu_id, mark, comment)
            # 如果运行程序报错，自动给60分
            except Exception as e:
                print(e)
                marks = marks.append({'stu_id': stu_id, 'mark': 60, 'comment': '代码报错'}, ignore_index=True)
                print('mark saved for ', stu_id, 60, '代码报错')
                input('是否开始下一位同学的代码？')

    if marks[marks.duplicated(['stu_id'])] is True:
        print('以下学生成绩有重复情况，需要注意')
        print(marks[marks.duplicated(['stu_id'])])
    # print(marks)

    marks.to_csv(os.path.join(py_files, 'mark_file.csv'), index=False, encoding='utf8')
    return marks



