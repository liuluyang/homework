

"""

1. 编写python程序，该程序可以创建一个文件，文件内容为一首唐诗。

2. 编写一个Python程序，读入第1题创建的唐诗文件，输出该唐诗文件中包含的字数和句数。

3. 编写一个python程序，程序读入python_zen.txt文件，
把其中句子顺序倒排后输出到另外一个文件python_zen_reverse.txt中。

4. 编写一个python程序，程序读入python_zen.txt文件，
提取该文件中所用到的单词组成的列表（即该文件用到了哪些不同的单词），
并把该单词列表输出到另外一个文件vocabulary.txt中。

5. 编写一个python程序，程序读入The Adventures of Tom Sawyer .txt文件，
提取该文件中所用到的单词组成的列表（即该文件用到了哪些不同的单词），
并统计每个单词的词频， 并把该词频表输出到另外一个文件frequency.txt中。

6. 编写一个Python程序，把所有和为100的三个正整数组合（三个数各不相同）输出到一个名为sum100.txt中.

7. score.csv文件中存放了每个同学计算机课考试试卷每个题目的得分(共4个题目)，
读入该文件，计算每个同学的总分，并把同学的学号、姓名和总分输出到另外一个文件final_score.csv中

8. 某学校规定，若课程成绩大于等于85分，成绩等级为优秀；若成绩大于等于60分且小于85分，成绩为及格；
若成绩小于60分，成绩等级为不及格。读入第7题中创建的final_score.csv文件，
根据其中的成绩为同学评定成绩等级，并把附加了成绩等级的同学成绩列表输出到名为level.csv文件中.
"""

def func_01():
    """

    :return:
    """
    text = '红豆生南国\t春来发几枝\n愿君多采撷\t此物最相思\n'

    with open('唐诗.txt', 'w', encoding='utf8') as f:
        f.write(text)

def func_02():
    """

    :return:
    """
    with open('唐诗.txt', 'r', encoding='utf8') as f:
        data = f.read()
        line_lst = data.split()
        words = ''.join(line_lst)
        return len(words), len(line_lst)


def func_03():
    """

    :return:
    """
    with open('python_zen.txt', 'rb') as f:
        with open('python_zen_reverse.txt', 'wb') as f_new:
            for line in f.readlines()[::-1]:
                f_new.write(line.strip() + b'\n')


def func_04():
    """

    :return:
    """
    import re
    import json

    with open('python_zen.txt', 'r', encoding='utf8') as f:
        words = re.findall('\w+', f.read())
        words_new = list(set(words))
        with open('vocabulary.txt', 'w') as f_new:
            json.dump(words_new, f_new)


def func_05():
    """

    :return:
    """
    import re
    import json

    with open('The Adventures of Tom Sawyer.txt', 'r', encoding='utf8') as f:
        words = re.findall('\w+', f.read())
        data = {}
        for w in words:
            if w in data:
                data[w] += 1
            else:
                data[w] = 1
        with open('frequency.txt', 'w') as f_new:
            json.dump(data, f_new)


def func_06():
    """

    :return:
    """
    with open('sum100.txt', 'w', encoding='utf8') as f:
        lst = []
        for x in range(101):
            for y in range(101 - x):
                z = 100 - x - y
                set_ = {x, y, z}
                if set_ not in lst and len(set_) == 3:
                    lst.append({x, y, z})
                    f.write(' '.join(map(lambda x:str(x), [x, y, z])) + '\n')


def func_07():
    """

    :return:
    """
    with open('score.csv', 'r', encoding='gbk') as f:
        f.readline()
        with open('final_score.csv', 'w', encoding='gbk') as f_new:
            f_new.write('学号,姓名,总分\n')
            for line in f:
                line_list = line.strip().split(',')
                score_num = sum([int(i) for i in line_list[2:]])
                f_new.write(','.join(line_list[:2] + [str(score_num)]) + '\n')


def func_08():
    """

    :return:
    """
    with open('final_score.csv', 'r', encoding='gbk') as f:
        f.readline()
        with open('level.csv', 'w', encoding='gbk') as f_new:
            f_new.write('学号,姓名,总分,成绩等级\n')
            for line in f:
                line_list = line.strip().split(',')
                score = int(line_list[-1])
                if score >= 85:
                    level = '优秀'
                elif score >= 60:
                    level = '及格'
                else:
                    level = '不及格'
                line_list.append(level)

                f_new.write(','.join(line_list) + '\n')


if __name__ == '__main__':
    pass
    # func_01()
    # print(func_02())
    # func_03()
    # func_04()
    # func_05()

    # func_06()

    # func_07()
    # func_08()