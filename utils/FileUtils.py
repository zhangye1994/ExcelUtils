import os

# 判断指定路径是文件还是目录
from utils import Printer as printer


def get_file_type(file_path):
    """
     返回指定路径文件类型
     文件：0 目录：1 其他：-1
    """
    if os.path.isfile(file_path):
        return 0
    elif os.path.isdir(file_path):
        return 1
    else:
        return -1


def get_file_paths(directory):
    """
     获取指定目录下所有文件完整路径集合
    """
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def get_dirs(directory):
    """
     获取指定目录下所有文件夹完整路径集合
    """
    dirs = []
    for root, directories, files in os.walk(directory):
        for directory_child in directories:
            filepath = os.path.join(root, directory_child)
            dirs.append(filepath)
    return dirs


def get_file_names(directory):
    """
     获取指定目录下所有文件和目录名集合
        1.不包含子目录下的文件和目录名
    """
    file_names = []
    files_and_folders = os.listdir(directory)
    for file_or_folder in files_and_folders:
        file_names.append(file_or_folder)
    return file_names


def rename(old_name, new_name):
    """
     重命名目录或者文件
    """
    try:
        if os.path.isfile(old_name):
            os.rename(old_name, new_name)
            printer.print_info(f"File {old_name} renamed to {new_name}")
        elif os.path.isdir(old_name):
            os.rename(old_name, new_name)
            printer.print_info(f"Directory {old_name} renamed to {new_name}")
        else:
            printer.print_warn(f"No such file or directory {old_name}")
    except Exception as e:
        printer.print_error(f"An error occurred: {e}")


def delete(directory):
    """
     删除指定目录及目录下所有子目录和文件
    """
    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                delete(file_path)
        os.rmdir(directory)
    else:
        printer.print_error("The directory does not exist.")
