


"""
1. 编写一个判断给定自然数是否素数的函数，调用该函数输出100以内的所有素数。

2. 编写一个能够计算两个给定自然数最大公因子的函数，
调用该函数计算用户输入的任何两个自然数的最大公因子。(可以采用辗转相除法计算最大公因子)

3. 编写一个能够判断给定自然数是否完全数的函数，
调用该函数输出1000以内的所有完全数。(完全数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的因子）之和，恰好等于它本身。
例如，6就是完全数，6的因子有1、2、3、6，除去本身6外，1+2+3=6)

4. 写一个函数计算某字符串中给定字符出现的次数，
调用该函数输出用户输入的字符串中给定字符出现的次数（函数要求提供两种实现，分别是非递归实现和递归实现）

5. 编写一个递归函数，该函数可以计算1+2+3+4+...+n的和。

6. 上台阶问题：有n级台阶，每步可以走一级或两级，问走完n级台阶有多少种不同走法，写一个递归函数完成计算。

7. 编写函数, 接收一个列表L(包含若干个整数)和一个整数k, 返回一个新列表，返回的新列表需要
        - 将列表下标k之前对应(不包含L[k])的元素逆序;
        - 将下标k及之后的元素逆序;

8. 将上述函数放在一个模块中，再写一个源程序文件，并在该源程序中实现对模块中函数的调用。
"""

def func_01():
    """

    :return:
    """
    nums = []

    for num in range(2, 101):

        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            nums.append(num)

    return nums


def func_02(a, b):
    """

    :return:
    """
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b

    return b


def func_03():
    """

    :return:
    """
    nums = []
    for num in range(1, 1000):
        count = 0
        for i in range(1, num):
            if num % i == 0:
                count += i
        if num == count:
            nums.append(num)

    return nums


def func_04(origin_s, target_s):
    """

    :param origin_s: 原始字符串
    :param target_s: 给定字符
    :return:
    """
    import re

    return len(re.findall(target_s, origin_s))


def func_05(n):
    """

    :param n:
    :return:
    """
    if n <=1:
        return 1

    return n + func_05(n - 1)


def func_06(n):
    """

    :param n:
    :return:
    """
    if n <= 1:
        return 1

    return func_06(n-1) +func_06(n-2)


def func_07(L, k):
    """

    :param L:
    :param k:
    :return:
    """

    return L[:k][::-1] + L[k:][::-1]


if __name__  ==  '__main__':
    # print(func_01())
    # print(func_02(100, 80))
    # print(func_03())
    # print(func_04('hello', 'e'))
    # print(func_05(100))
    # print(func_06(5))
    # print(func_07([1, 2, 3, 4, 5], 2))
    pass
