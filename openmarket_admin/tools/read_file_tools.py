# 读取文件的通用工具
import csv
import xlrd


class ReadFileUtils:
    @classmethod
    def readExcel(cls, file_path, sheet_name="Sheet1", has_title=True):
        '''
        读取excel中的测试数据
        :param file_path:  excel文件路径
        :param sheet_name:  工作簿名
        :param has_title: 是否有表头
        :return: has_title=True返回字典组成的列表，否则返回列表组成的列表
        '''
        datas = []  # 所有数据的列表
        # 打开指定路径中的工作簿
        book = xlrd.open_workbook(file_path, "r")
        # 读取对应工作表
        sheet = book.sheet_by_name(sheet_name)
        if has_title:  # 读取表头， 返回的是字典组成的列表
            keys = sheet.row_values(0)  # 读取表头
            # 循环读取数据 从第一行有效数据开始 到最后一行有效数据
            for row_num in range(1, sheet.nrows):
                # 读取出指定行的所有值 - 所有数据 是列表
                values = sheet.row_values(row_num)
                dt_row = {}  # 每一行数据的字典
                # 根据这一行中数据的数量，决定循环次数
                for i in range(0, len(values)):
                    # 把这一列的表头 与 这一列的值 组合成字典的一个数据
                    dt_row[keys[i]] = values[i]
                # 把一行数据的字典，追加到所有数据的列表中
                datas.append(dt_row)
        else:  # 不读取表头，返回的是列表组成的列表
            # 循环 从0开始到最后一行
            for i in range(0, sheet.nrows):
                # 读取每一行的数据
                row = sheet.row_values(i)
                # 把每一行追加到 所有数据的列表中
                datas.append(row)
        return datas

    @classmethod
    def readCSV(cls, file_path, has_title=True):
        '''
        读取csv文件中的数据
        :param file_path: csv文件地址
        :param has_title:  是否有表头
        :return: has_title=True返回字典组成的列表，否则返回列表组成的列表
        '''
        datas = []  # 存储所有数据的列表
        with open(file_path, "r", encoding="utf8") as f:
            data = csv.reader(f)  # 通过csv读取文件中的数据
            if has_title:  # 是否有标题，有标题 返回的是字典组成的列表
                isfirst = True  # 是否第一行
                for row in data:  # 读取所有数据
                    if isfirst:  # 第一行数据
                        keys = row  # 读取后做字典的关键字
                        isfirst = False  # 关闭第一行的开关
                    else:  # 读取之后所有行
                        dt = {}  # 每一行数据的字典
                        # 根据这一行中数据的个数决定循环次数
                        for i in range(len(row)):
                            # 把这一列的表头与这一列的值 组合成字典的一个数据
                            dt[keys[i]] = row[i]
                        # 把这一行数据的字典追加到所有数据的列表中
                        datas.append(dt)
            else:  # 没有标题（表头） 返回的是列表组成的列表
                # 循环读取所有数据 读出来的就是一行数据的列表
                for row in data:
                    # 把这一行数据的列表 追加到所有数据的列表中
                    datas.append(row)
        return datas  # 返回所有数据


if __name__ == "__main__":
    # data = ReadFileUtils.readExcel("./test_data/login.xlsx",has_title=False)
    data = ReadFileUtils.readCSV("./test_data/login.csv")
    print(data)
