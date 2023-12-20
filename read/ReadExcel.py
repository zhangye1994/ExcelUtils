import xlrd
import xlrd.sheet as xlrd_sheet


# 获取excel所有的sheets的名称
def get_sheet_names(file):
    wb = xlrd.open_workbook(file)
    sheets = wb.sheet_names()
    return sheets


# 打开Sheet
def read_sheet(file, sheet_name):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_name(sheet_name)
    return sheet


# 获取excel表格总行数
def get_rows(file, sheet_name):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_name(sheet_name)
    return sheet.nrows


# 获取excel表格列数
def get_columns(file, sheet_name):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_name(sheet_name)
    return sheet.ncols


# 获取首行对应字段所在列号
def get_columns_by_name(sheet: xlrd_sheet, column_names):
    columns = sheet.ncols
    column_index = {}
    for index in range(0, columns):
        column_value = get_single_value(sheet, 0, index)
        column_index[column_value] = index
    column_nums = []
    for name in column_names:
        column_nums.append(column_index[name])
    return column_nums


# 根据行列号获取对应的值
def get_single_value(sheet: xlrd_sheet, row, col):
    value = sheet.cell_value(row, col)
    if value is None:
        return ""
    return str(value)


# 获取excel所有行数据
def get_rows_value(sheet: xlrd_sheet):
    row_values = sheet.get_rows()
    row_result = []
    for row_item in row_values:
        row_result.append(row_item)
    return row_result


# 获取excel所有数据
def get_all_value(sheet: xlrd_sheet):
    row_values = sheet.get_rows()
    row_result = []
    for row_item in row_values:
        for value in row_item:
            row_result.append(value)
    return row_result
