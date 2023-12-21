# 定义一个函数来输出不同颜色的文本  
def print_colored_text(text, color):
    print('\033[{}m{}\033[0m'.format(color, text))


# 提示信息以蓝色字体打印
def print_info(text):
    print_colored_text(text, 94)


# 告警信息以黄色字体打印
def print_warn(text):
    print_colored_text(text, 33)


# 错误信息以红色字体打印
def print_error(text):
    print_colored_text(text, 91)
