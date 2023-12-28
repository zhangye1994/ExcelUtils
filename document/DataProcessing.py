def data_compare(data_list1, index1, data_list2, index2):
    """
    在data_list2中查找与data_list1中对应下标数据能匹配上的数据
    将匹配成功的data_list2数据放到data_list1后面作为一个新的item输出到结果中
        :param data_list1: 表格数据集1，格式要求为二维数组
        :param index1: 下标1
        :param data_list2: 表格数据集2，格式要求为二维数组
        :param index2: 下标2
        :return: 将两个表中能够匹配的数据进行合并输出为一个新的集合
    """
    data_list1 = sorted(data_list1, key=lambda x: x[index1])
    data_list2 = sorted(data_list2, key=lambda x: x[index2])
    result = []
    for data1 in data_list1:
        for data2 in data_list2:
            if str(data1[index1]).__contains__(str(data2[index2])):
                result.append(data1 + data2)
    return result
