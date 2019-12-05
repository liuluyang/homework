


def check_id_card():
    """
    身份证号检测
    :return:
    """
    check_num = '7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2'
    check_num = [int(s) for s in check_num.split(',')]
    last_num_list = list('10X98765432')

    while True:
        num_card = input('请输入身份证号：')

        if len(num_card) != 18:
            print('身份证号码位数错误！')
            continue

        count = 0
        for one, two in zip(num_card[:-1], check_num):
            count += int(one) * two

        last_num = last_num_list[count % 11]
        if last_num == num_card[-1]:
            print('身份证号正确')
            break
        else:
            print('身份证号非法,请重新输入！')


def func_02(res01, res02):
    """

    :param res01:
    :param res02:
    :return:
    """

    count = 0
    res01_set = set(res01)

    for s in res02:
        if s in res01_set:
            count += 1

    return count


def func_03(nums, target):
    """

    :param nums:
    :param target:
    :return:
    """

    nums_index_dict = {}
    for index, num in enumerate(nums):
        if num in nums_index_dict:
            nums_index_dict[num].append(index)
        else:
            nums_index_dict[num] = [index]

    for n in nums:
        other = target - n
        if other in nums_index_dict:
            index_02 = nums_index_dict[other][-1]
            index_01 = nums_index_dict[n][0]
            return [index_01, index_02]


if __name__ == '__main__':
    # check_id_card()
    # print(func_02('z', 'Z'))
    # print(func_03([2, 7, 11, 15], 9))
    pass
