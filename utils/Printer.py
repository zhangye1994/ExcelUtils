def print_colored_text(text, color):
    """
    定义一个函数来输出不同颜色的文本

    :param text: 提示文本
    :return: Non
    """
    print('\033[{}m{}\033[0m'.format(color, text))


def print_info(text):
    """
    提示信息以蓝色字体打印

    :param text: 提示文本
    :return: Non
    """
    print_colored_text(text, 94)


def print_warn(text):
    """
    告警信息以黄色字体打印

    :param text: 提示文本
    :return: Non
    """
    print_colored_text(text, 33)


def print_error(text):
    """
    错误信息以红色字体打印

    :param text: 提示文本
    :return: Non
    """
    print_colored_text(text, 91)
