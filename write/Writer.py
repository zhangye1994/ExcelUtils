import numpy
import xlsxwriter as writer

from utils import Printer
from write.FormatConfiguration import FormatConfiguration


class ExcelWriter:
    wb = None
    sheets = {}

    def __init__(self, target_file):
        self.wb = writer.Workbook(target_file)

    def add_worksheet(self, sheet_name):
        """
        添加sheet

        :param sheet_name: sheet名称
        :return: ExcelWriter自身
        """
        self.sheets[sheet_name] = self.wb.add_worksheet(sheet_name)
        return self

    def write_all(self, sheet_name, data):
        """
        将二维数组所有数据写入到指定sheet中

        :param sheet_name: sheet名
        :param data: 二维数组数据集合
        :return: 对象自身
        """
        if numpy.array(data).ndim != 2:
            Printer.print_error("数据类型错误")
            return self
        if not self.sheets.keys().__contains__(sheet_name):
            self.add_worksheet(sheet_name)
        sheet = self.sheets[sheet_name]
        for row in range(0, len(data)):
            for column in range(0, len(data[row])):
                sheet.write_row(row, column, data[row][column])
        return self

    def write_by_column(self, sheet_name: str, data, column_index):
        """
        将data数据中指定的列数据写入到sheet中

        :param sheet_name: sheet名
        :param data: 数据
        :param column_index: 指定写入列
        :return: 对象自身
        """
        if numpy.array(data).ndim != 2:
            Printer.print_error("数据类型错误")
            return self
        if numpy.array(column_index).ndim != 1:
            Printer.print_error("索引类型错误")
            return self
        if not self.sheets.keys().__contains__(sheet_name):
            self.add_worksheet(sheet_name)
        sheet = self.sheets[sheet_name]
        for row in range(0, len(data)):
            for column in column_index:
                sheet.write(row, column, data[row][column])
        return self

    def set_width(self, sheet_name, column, width=20):
        """
        设置worksheet指定列宽度

        :param sheet_name: sheet名
        :param column: 指定列
        :param width: 指定宽度
        :return: 对象自身
        """
        self.sheets[sheet_name].set_column(column, width)
        return self

    def set_height(self, sheet_name, row, height=20):
        """
        设置worksheet指定列宽度

        :param sheet_name: sheet名
        :param row: 指定行
        :param height: 指定高度
        :return: 对象自身
        """
        if not self.sheets.keys().__contains__(sheet_name):
            self.add_worksheet(sheet_name)
        self.sheets[sheet_name].set_row(row, height)
        return self

    def format(self, formatted=FormatConfiguration()):
        """
       采用链式调用的方式设置表格的样式

        :param formatted: 指定样式配置
        :return: 对象自身
        """
        self.wb.add_format(formatted.formatted_text)
        return self

    def save(self):
        """
        writer需要调用关闭方法后才会保存文档

        :return: Non
        """
        self.wb.close()
