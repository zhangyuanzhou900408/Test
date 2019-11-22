import xlrd
from xlutils.copy import copy
# data = xlrd.open_workbook('../dataconfig/API.xlsx')
# tables = data.sheets()[0]
# print(tables.nrows)
# print(tables.cell_value(1,1))

class OperationExcel:
     def __init__(self,file_name,sheet_id):
         if file_name:
             self.file_name =file_name
             self.sheet_id = sheet_id
         else:
             self.file_name = '../dataconfig/API.xls'
             self.sheet_id = 0
         self.data = self.get_data()

     #获取某一页sheet对象
     def get_data(self):
         data = xlrd.open_workbook(self.file_name)
         tables = data.sheets()[self.sheet_id]
         return tables
     # 获取excel数据行数
     def get_rows(self):
         rows = self.data.nrows
         return rows
     # 获取某个单元格某行或者某列的数据
     def get_value(self,row,col):
         value = self.data.cell_value(row,col)
         return value

         # 复制excel数据 ,导入数据到excel中
     def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name) # 打开源文件
        write_data = copy(read_data)   # 复制文件
        sheet_data = write_data.get_sheet(0) #获取复制文件的第一个单元表
        sheet_data.write(row,col,value) # 让往第一个单元表中的指定行列写入数据
        write_data.save(self.file_name)  # 保存数据
        return value  # 返回修改的值






if __name__ == '__main__':
    file_name = '../dataconfig/API.xls'
    opers = OperationExcel(file_name=file_name,sheet_id = 0)
    print(opers.get_rows())
    print(opers.get_value(1,2))
    print(opers.write_value(3, 4, "post"))
