import win32com.client as win32


def shut_excel():
    # 打开Excel应用程序
    excel = win32.Dispatch("Excel.Application")
    # 关闭Excel应用程序
    excel.Quit()


def close_active_word():
    # 获取已打开的Word应用程序实例
    word = win32.GetActiveObject("Word.Application")
    # 获取要关闭的文档
    doc = word.ActiveDocument
    # 关闭文档
    doc.Close()
    # 退出Word应用程序
    word.Quit()
