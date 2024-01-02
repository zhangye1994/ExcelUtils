from read.OlderReader import OlderReader
from read.NewerReader import NewerReader


def create_reader(file_path: str):
    """"
        根据类型获取不同Reader对象

        OlderReader当前支持：.xlt,.xls等

        NewerReader当前支持：.xlsx,.xlsm,.xltx,.xltm等
    """
    if file_path is None or len(file_path.strip()) == 0:
        raise Exception("File path is empty!")
    if file_path.endswith(".xls") or file_path.endswith(".xlt"):
        return OlderReader(file_path)
    return NewerReader(file_path)
