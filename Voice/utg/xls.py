import xlrd
from xlutils.copy import copy
#操作Excel表格数据
class OperationExecl:
    def __init__(self,file_name,sheet_id):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'F:\\HF.xls'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取表单sheet
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取行数
    def get_rows(self):
        row = self.data.nrows
        return row
    # 获取行数
    def get_cols(self):
        col = self.data.ncols
        return col

    #获取表单数据

    def get_value(self,row,col):
        value = self.data.cell_value(row,col)
        return value

    # 导入数据
    def write_data(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = self.data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
        return value

