from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def get_sheet_names(self):
        """
        获取当前workbook所有的sheet名称

        :return: sheet名称集合
        """
        pass

    @abstractmethod
    def open_sheet(self, sheet_name):
        """
        打开指定名称Sheet

        :param sheet_name: sheet名称
        :return: 返回sheet
        """
        pass

    @abstractmethod
    def get_rows(self, sheet_name):
        """
        获取excel表格行数

        :param sheet_name: sheet名称
        :return: 行数
        """
        pass

    @abstractmethod
    def get_columns(self, sheet_name: str):
        """
        获取excel表格列数

        :param sheet_name: sheet名称
        :return: 列数
        """
        pass

    @abstractmethod
    def get_columns_by_name(self, sheet_name: str, column_names, row_line=0):
        """
        获取指定行对应列值所在列号

        :param row_line: 从指定行读取对应的列值，默认首行
        :param sheet_name: sheet名称
        :param column_names: 列名
        :return: 以字典格式返回对应字段所在的列
        """
        pass

    @abstractmethod
    def get_single_value(self, sheet_name: str, row, col) -> str:
        """
        根据行列号获取对应的值

        :param sheet_name: sheet名称
        :param row: 行号
        :param col: 列号
        :return: 对应的值，为空时返回空串，避免类型异常
        """
        pass

    @abstractmethod
    def get_row_values(self, sheet_name: str):
        """
        按行读取Excel所有数据

        :param sheet_name: sheet名称
        :return: 二维数组格式Excel数据
        """
        pass

    @abstractmethod
    def get_column_values(self, sheet_name: str, column_index):
        """
        按列读取Excel所有数据

        :param sheet_name: sheet名称
        :param column_index: 对应的列名索引数组
        :return: 二维数组格式Excel数据
        """
        pass

    @abstractmethod
    def get_all_value(self, sheet_name: str):
        """
        按行列逐个获取excel所有数据

        :param sheet_name: sheet名称
        :return: 一维数组格式Excel数据
        """
        pass

    @abstractmethod
    def close(self):
        """
        关闭工作簿
        封装原始代码，闭环整个Reader

        :return: NA
        """
        pass
