


"""
1. 写程序打印自己名字的UNICODE、UTF-8、GB18030的编码。

2. score.csv文件中存放了每个同学计算机课考试试卷每个题目的得分(共4个题目)，
读入该文件，计算每个同学的总分，并把同学的学号、姓名、每个题目的得分、
总分输出按照总分从高到低的顺序输出至另外一个文件score.txt，要求使用格式字符串控制输出的样式。

3. 给定的文件“红楼梦.txt”采用utf-8编码格式，编写python程序生成一个以gb18030编码形式存放的红楼梦文件。
观察文件长度有什么变化，解释长度变化的原因。

4. 编写python程序，统计红楼梦中每个字出现的频率生成字频表，要求字频表按照频次由高到低排序，
并以文件的形式输出字频表。（统计字频要求使用字典类型）

5. ‘list.csv’文件给出了汉语中汉字、拼音和笔画数的对应关系，请利用这个文件，
重做第2题，使其生成按姓名音序、笔画序及分数序的三种成绩表。
"""

def func_01(name='我的名字'):
    """

    :param name:
    :return:
    """

    name_u = name.encode(encoding='unicode_escape')
    name_utf8 = name.encode(encoding='UTF-8')
    name_gbk = name.encode(encoding='GB18030')

    return name_u, name_utf8, name_gbk


def func_02():
    """

    :return:
    """
    with open('score.csv', 'r', encoding='gbk') as f:
        f.readline()
        with open('score.txt', 'w', encoding='utf8') as f_new:
            score_data = []
            for line in f:
                line_list = line.strip().split(',')
                score_num = sum([int(i) for i in line_list[2:]])
                line_list.append(score_num)
                score_data.append(line_list)
            score_data.sort(key=lambda x:x[-1], reverse=True)
            for line_list in score_data:
                line_new = '学号：%s    姓名：%s%s得分：%s    总分：%s\n'%(
                    line_list[0].zfill(2), line_list[1], '  '*(6-len(line_list[1])),
                    ','.join(line_list[2:-1]), str(line_list[-1]))
                f_new.write(line_new)


def func_03():
    """
    解释：
        把以utf8编码的红楼梦.txt 编码成GB18030编码的文件后
        文件占用的空间变小了, 大小变成了原来的三分之二左右
        因为一个汉字的utf8编码占三个字节，而gbk编码占两个字节
        例子：
        print('中'.encode())                 # b'\xe6\x80\xbb'
        print('中'.encode(encoding='gbk'))   # b'\xd7\xdc'
    :return:
    """
    with open('红楼梦.txt', 'r', encoding='utf8') as f:
        with open('红楼梦_gb18030.txt', 'w', encoding='GB18030') as f_new:
            f_new.write(f.read())


def func_04():
    """

    :return:
    """
    import re

    with open('红楼梦.txt', 'r', encoding='utf8') as f:
        content = f.read()
        words = re.findall('\w', content)
        words_dict = {}
        for w in words:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1
        words_dict_sorted = sorted(words_dict.items(), key=lambda x:x[-1], reverse=True)
        with open('红楼梦-字频表.txt', 'w', encoding='utf8') as f_new:
            for d in words_dict_sorted:
                f_new.write(' '.join([str(i) for i in d]) + '\n')


def func_05():
    """

    :return:
    """
    sort_dict = {}
    with open('list.csv', 'r', encoding='gbk') as f:
        for index, line in enumerate(f):
            line_list = line.split(',')
            sort_dict[line_list[0]] = [index, int(line_list[-1])]

    with open('score.csv', 'r', encoding='gbk') as f:
        f.readline()
        score_data = []
        for line in f:
            line_list = line.strip().split(',')
            score_num = sum([int(i) for i in line_list[2:]])
            line_list.append(score_num)
            score_data.append(line_list)


        def inner(score_data, f_new):

            for line_list in score_data:
                line_new = '学号：%s    姓名：%s%s得分：%s    总分：%s\n'%(
                    line_list[0].zfill(2), line_list[1], '  '*(6-len(line_list[1])),
                    ','.join(line_list[2:-1]), str(line_list[-1]))
                f_new.write(line_new)

        # 按音序
        with open('score-音序.txt', 'w', encoding='utf8') as f_new:
            score_data.sort(key=lambda x:sort_dict[x[1][0]][0])
            inner(score_data, f_new)

        # 按笔画序
        with open('score-笔画序.txt', 'w', encoding='utf8') as f_new:
            score_data.sort(key=lambda x:sort_dict[x[1][0]][1])
            inner(score_data, f_new)

        # 按分数序
        with open('score-分数序.txt', 'w', encoding='utf8') as f_new:
            score_data.sort(key=lambda x:x[-1])
            inner(score_data, f_new)

if __name__ == '__main__':
    # print(func_01())
    # func_02()
    # func_03()
    # func_04()
    # func_05()
    pass