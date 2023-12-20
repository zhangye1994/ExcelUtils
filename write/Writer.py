import xlsxwriter


# 将数据写入到指定文件的指定sheet中
def write(des_file, sheet_name, data):
    wb = xlsxwriter.Workbook(des_file)
    sheet = wb.add_worksheet(sheet_name)
    for row in range(0, len(data)):
        for column in range(0, len(data[row])):
            sheet.write(row, column, data[row][column])
    wb.close()
