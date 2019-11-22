import xlrd
import re
#把Excel内容进行转换单条资源导入txt文档中
def read_xlsx():
    #打开文件
    data = xlrd.open_workbook("F:\\Voices\\33.xls")
    #print(data)
    table = data.sheet_by_name("Sheet1") #打开第一张表
    #print(table)
    rows = table.nrows   #获取行数
    #print(rows)
    ncols = table.ncols  #获取列数
    #print(ncols)
    row_list = []
    for i in range(0, rows):
        #print(i)
        row_data = table.row_values(i)
        row_list.append(row_data)
    #print(row_list)
    f = open('F:\\00.txt',"ab")
    #print(rows)
    #print(ncols)
    for rowNum in range(rows):
        tmp = ""
        print(rowNum)
        for colNum in range(0, ncols):
            if  table.cell(rowNum, colNum).value != None:
              tmp += str( table.cell(rowNum, colNum).value)# + u"\t"
        tmp += "\n"
        #print(tmp)
        data = f.write(tmp.encode('utf-8'))
    #print(data)





#if __name__ == '__main__':
   # read_xlsx()
