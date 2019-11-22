import yaml
import pymysql
import json
import  xlrd
class Test_yaml:
    def get_test(self):
        with open("F:\\test\dataconfig\\test.yaml", 'r', encoding='utf-8')as f :
            page =yaml.load(f)
            print(page)
            dm = page["Addanapp"]
            print(dm)
            tm = dm["xpath"]
            print(tm)
cm = Test_yaml()
#cm.get_test()
# 连接数据库及查询
# com = pymysql.connect(
# host="172.16.225.142",
# port = "3306",
# user = "APIDB",
# passwd = "123456",
# db = "HFMedia",
# charset = "utf-8"
# )
# cur = com.cursor()
# url = cur.execute("select songurl from HFSongs ")
# print(url)
# 操作xlsx
file_name = "F:\\Voices\\33.xls"
data_name = xlrd.open_workbook(file_name)
sheet_data = data_name.sheets()[0]
row = sheet_data.nrows
print(row)
line = sheet_data.ncols
print(line)
data = data_name.cell_value(1,1)



