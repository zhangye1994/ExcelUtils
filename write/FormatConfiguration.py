from write.HorizontalAlign import HorizontalAlign
from write.VerticalAlign import VerticalAlign


class FormatConfiguration:
    formatted_text = {}

    def set_bg_color(self, color="#000000"):
        """
        设置背景颜色

        :param color: 颜色值十六进制or名称
        :return: 对象自身
        """
        self.formatted_text["bg_color"] = color
        return self

    def set_border_color(self, color="#000000"):
        """
        设置边框颜色

        :param color: 颜色值十六进制or名称
        :return: 对象自身
        """
        self.formatted_text["border_color"] = color
        return self

    def set_delete_color(self, color="#000000"):
        """
        设置删除线颜色

        :param color: 颜色值十六进制or名称
        :return: 对象自身
        """
        self.formatted_text["delete_color"] = color
        return self

    def set_font_color(self, color="#000000"):
        """
        设置字体颜色

        :param color: 颜色值十六进制or名称
        :return: 对象自身
        """
        self.formatted_text["font_color"] = color
        return self

    def set_pattern_fore_color(self, color="#000000"):
        """
        设置前景颜色

        :param color: 颜色值十六进制or名称
        :return: 对象自身
        """
        self.formatted_text["pattern_fore_color"] = color
        return self

    def set_font_name(self, font_name="Arial"):
        """
        设置字体

        :param font_name: 字体名
        :return: 对象自身
        """
        self.formatted_text["font_name"] = font_name
        return self

    def set_font_size(self, font_size=10):
        """
        设置字体大小

        :param font_size: 字体大小
        :return: 对象自身
        """
        self.formatted_text["font_size"] = font_size
        return self

    def set_bold(self, bold=True):
        """
        设置字体是否加粗

        :param bold: True或者False
        :return: 对象自身
        """
        self.formatted_text["bold"] = bold
        return self

    def set_horizontal_align(self, align=HorizontalAlign.CENTER):
        """
        设置字体水平对齐模式

        :param align: 水平居中方式
        :return: 对象自身
        """
        self.formatted_text["align"] = align
        return self

    def set_vertical_align(self, align=VerticalAlign.CENTER):
        """
        设置字体垂直对齐模式

        :param align: 垂直居中方式
        :return: 对象自身
        """
        self.formatted_text["valign"] = align
        return self

    def set_border(self, border=1):
        """
        设置边框宽度

        :param border: 垂直居中方式
        :return: 对象自身
        """
        self.formatted_text["border"] = border
        return self

    def set_shadow(self, shadow=True):
        """
        设置阴影

        :param shadow: 是否设置阴影
        :return: 对象自身
        """
        self.formatted_text["shadow"] = shadow
        return self

    def set_shadow_offset(self, x=0, y=0):
        """
        设置阴影的颜色和偏移量

        :param x: 横向偏移
        :param y: 纵向偏移
        :return: 对象自身
        """
        self.formatted_text["shadow_offset"] = (x, y)
        return self

    def add_delete_line(self, is_add=True):
        """
        添加删除线

        :param is_add: 是否添加
        :return: 对象自身
        """
        self.formatted_text["delete"] = is_add
        return self

    def set_indent(self, indent=0):
        """
        设置缩进

        :param indent: 缩进值
        :return: 对象自身
        """
        self.formatted_text["indent"] = indent
        return self

    def set_text_wrap(self, wrap=True):
        """
        设置自动换行

        :param wrap: 是否自动换行
        :return: 对象自身
        """
        self.formatted_text["text_wrap"] = wrap
        return self

    def set_pattern(self, pattern=0):
        """
        设置图案样式

        :param pattern: 0：无图案 1：10%的灰色 2：25%的灰色 3：50%的灰色 4：20%的浅色网格 ：交叉阴影
        :return: 对象自身
        """
        self.formatted_text["pattern"] = pattern
        return self

    def set_locked(self, is_lock=True):
        """
        设置单元格是否受保护

        :param is_lock: 单元格是否受保护
        :return: 对象自身
        """
        self.formatted_text["is_lock"] = is_lock
        return self
