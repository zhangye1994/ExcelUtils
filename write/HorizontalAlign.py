from enum import Enum


class HorizontalAlign(Enum):
    """
    'left'：文本左对齐。

    'center'：文本居中对齐。

    'right'：文本右对齐。

    'fill'：文本填充对齐（在合并单元格中比较有用,可以让文本充满整个单元格）。

    'justify'：文本两端对齐（在某些情况下，可能需要配合换行使用）。
    """
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'
    FILL = 'fill'
    JUSTIFY = 'justify'