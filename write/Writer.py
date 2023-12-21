import numpy
import xlsxwriter as writer

from ExcelUtils.utils import Printer


class ExcelWriter:
    wb = None
    sheets = {}

    # 将数据写入到指定文件的指定sheet中
    def create(self, des_file, sheet_name):
        self.wb = writer.Workbook(des_file)
        self.sheets[sheet_name] = self.wb.add_worksheet(sheet_name)
        return self

    def write_all(self, sheet_name, data):
        if numpy.array(data).ndim == 2:
            Printer.print_error("数据类型错误")
            return self
        sheet = self.sheets[sheet_name]
        for row in range(0, len(data)):
            for column in range(0, len(data[row])):
                sheet.write(row, column, data[row][column])
        self.sheets[sheet_name] = sheet
        return self

    # 采用链式调用的方式设置表格的样式
    def format(self, format_json=None):
        self.wb.add_format(format_json)

    # writer需要调用关闭方法后才会保存文档
    def save(self):
        self.wb.close()
