# ExcelUtils
####自述
    工作量的增加，让自己决心写一个报表处理工具以适应自己的日常工作并不断完善，一个人的需求是狭隘的、片面的
    希望能够收到来自不同行业的大佬的issue，以使得这个工具更加强大，可以支撑更加复杂的工作

####当前支持的能力

    1.自动提取指定excel文件数据后生成新的excel
        1.1按列号提取
        1.2按首行字段名提取
            拆分需求
            1.2.1根据首行字段名获取到对应的列号
            1.2.2再通过列号提取对应的数据
        
    2.在B表中查找与A表匹配的数据，追加的A表对应记录后并备注匹配类型
        2.1单列匹配
        2.2多列匹配
        2.3匹配类型        
            2.3.1完全匹配            
            2.3.2包含匹配            
            2.3.3优先完全匹配，不成功再进行包含匹配            
        2.4需求理解：        
            数据：A表中存在姓名，年龄，个人信息概述，B表中存在姓名，性别，班级信息            
            要求：在B表中提取出姓名，性别，班级信息追加到A表对应的记录中    
            
    3.解决各种Excel格式兼容的问题

    4.支持设置表格格式化

    6.支持日志打印
        当前设置三种级别提示信息：error（红）warning（黄）info（蓝）