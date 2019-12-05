


"""
文计第八次作业
"""


def func_01(res):
    """
    单词排序
    :param res: 含有英文单词的字符串
    :return:
    """
    def rule(w):
        """
        排序规则
        :param w:
        :return:
        """

        return tuple(w[-i-1] for i in range(len(w)))

    word_list = res.split()

    word_list_new = sorted(word_list, key=rule, reverse=True)

    return word_list_new


def func_02():
    """
    按第一科成绩从小到大 排序score.csv文件
    :return:
    """
    with open('score.csv', 'r', encoding='gbk') as f:
        title = f.readline()
        data = [line.split(',') for line in f.readlines()]
        data.sort(key=lambda x:x[2])
        with open('score_sorted.csv', 'w', encoding='gbk') as f_new:
            f_new.write(title)
            for line in data:
                f_new.write(','.join(line))


def func_03(n):
    """
    打印杨辉三角
    :param n:
    :return:
    """
    def make_lst(lst):

        lst_new = []
        for index in range(len(lst) - 1):
            lst_new.append(lst[index] + lst[index + 1])

        return [1] + lst_new + [1]

    lst = [1]
    if n >= 1:
        print(' '.join([str(i) for i in lst]))

    for i in range(n - 1):
        lst_next = make_lst(lst)
        print(' '.join([str(i) for i in lst_next]))
        lst = lst_next


def func_04(M, N):
    """
    分苹果
    M个苹果、N个盘子
    :return:
    """
    if M== 0 or N == 1:
        return 1
    elif M < N:
        return func_04(M, M)
    else:
        return func_04(M, N-1) + func_04(M-N, N)


if __name__ == '__main__':
    pass
    # print(func_01())
    # func_02()
    # func_03(7)
    # print(func_04(10, 2))





