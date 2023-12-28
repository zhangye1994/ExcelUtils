import numpy
import xlsxwriter as writer

from utils import Printer


class ExcelWriter:
    wb = None
    sheets = {}

    def __init__(self, target_file):
        self.wb = writer.Workbook(target_file)
        return self

    def add_worksheet(self, sheet_name):
        """
        添加sheet
        :param sheet_name:
        :return:
        """
        self.sheets[sheet_name] = self.wb.add_worksheet(sheet_name)
        return self

    def write_all(self, sheet_name, data):
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
        :return: writer自身
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

    # 采用链式调用的方式设置表格的样式
    def format(self, format_json=None):
        self.wb.add_format(format_json)

    # writer需要调用关闭方法后才会保存文档
    def save(self):
        self.wb.close()
