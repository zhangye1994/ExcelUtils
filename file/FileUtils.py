import os


# 判断指定路径是文件还是目录
def get_file_type(file_path):
    if os.path.isfile(file_path):
        return 0
    elif os.path.isdir(file_path):
        return 1
    else:
        return -1


# 获取指定目录下所有文件完整路径集合
def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


# 获取指定目录下所有文件夹完整路径集合
def get_dirs(directory):
    dirs = []
    for root, directories, files in os.walk(directory):
        for directory_child in directories:
            filepath = os.path.join(root, directory_child)
            dirs.append(filepath)
    return dirs


# 获取指定目录下所有文件和目录名集合
def get_file_names(directory):
    file_names = []
    files_and_folders = os.listdir(directory)
    for file_or_folder in files_and_folders:
        file_names.append(file_or_folder)
    return file_names


# 重命名目录或者文件
def rename(old_name, new_name):
    try:
        if os.path.isfile(old_name):
            os.rename(old_name, new_name)
            print(f"File {old_name} renamed to {new_name}")
        elif os.path.isdir(old_name):
            os.rename(old_name, new_name)
            print(f"Directory {old_name} renamed to {new_name}")
        else:
            print(f"No such file or directory {old_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete(directory):
    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件
            elif os.path.isdir(file_path):
                delete(file_path)  # 递归删除子目录
        os.rmdir(directory)  # 删除空目录
    else:
        print("The directory does not exist.")
