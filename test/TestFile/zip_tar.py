import zipfile
import time
from collections import Counter
import pygal
from random import randint
import xlrd
import xlwt
#压缩文件
# z=zipfile.ZipFile("K:\\tet.gz","w")
# z.write("G:\\app_log\\crash_launcher_d9\\crash-2019-10-15-02-48-20-1571078900067.txt")
# z.write("G:\\app_log\\crash_launcher_d9\\crash-2019-10-15-11-56-44-1571111804354.txt")
# z.close()
#解压文件
# z=zipfile.ZipFile("K:\\tet.gz","r")
# z.extractall(path='K:\\tet')
# z.close()
# print(time.ctime(time.time()))
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# d= time.strptime('23 Oct 2017','%d %b %Y')
# print(d)
# print(time.asctime(d))
# list = []
# frequencies= []
# for i in range(100):
#     results = randint(1, 50)
#     list.append(results)
# #print(list)
# for i in range(6):
#     data = list.count(i)
#     data = frequencies.append(data)
# print(frequencies)
# #处理結果
# hist = pygal.Bar() #生存实例
# hist.title = 'Results of rolling one D6 1000 times' # 图的标题
# hist.x_labels = ["1","2","3","4","5","6"]  # 生产X抽的值
# hist.y_title = "对应的数字竖状图"
# hist.x_title = "Result"
# hist.add("D6",frequencies) #添加数据
# hist.render_to_file("../TestFile/die_visual.svg")  #保存文件
# hiet = pygal.Pie()
# hiet.title="年龄段饼状图测试结果"
# hiet.add("1-10",8)
# hiet.add("10-20",2)
# hiet.add("20-30",10)
# hiet.add("30-40",12)
# hiet.add("40-50",8)
# hiet.add("50-60",10)
# hiet.add("60-70",12)
# hiet.add("70-80",8)
# hiet.add("80-90",10)
# hiet.add("990-90",10)
# hiet.add("80-90",10)
# hiet.render_to_file("../TestFile/Age_Distribution.svg")
# sheet = xlwt.Workbook(encoding="ascii")
# datasheet = sheet.add_sheet("mytest")
# datasheet.write(0, 0, label='Row 0, Column 0 Value')
# data = sheet.save("./test.xls")
# print(data)
# readsheet = xlrd.open_workbook(r"./test.xls")
# sheet = readsheet.sheet_by_name("mytest")
# nrows = sheet.nrows#行
# ncols = sheet.ncols#列
# print(nrows)
# print(ncols)
# sheet_lng = sheet.cell(0,1).value
# print(sheet_lng)
# print(time.mktime(time.localtime()))
# print(time.time())
# print(time.localtime())
# print(time.ctime(time.time()))
# print(time.strftime("%Y-%m-%d %X",time.localtime()))
# data = time.strptime('2011-05-05 18:15:32', '%Y-%m-%d %X')
# print(time.asctime(data))
# print(time.asctime(time.localtime()))
# print(time.ctime(time.time()))
# print(time.mktime(time.localtime()))
# print(time.strftime('%Y-%m-%d %X',time.localtime()))
# str = "zhangyuanzhounizuimei"
# date = Counter(str)
# from datetime import  datetime
# print(datetime.now())
# print(datetime(2019,12,30,18,35,40))
# print(datetime(2019,12,30,18,35,40).timestamp())  # time 转换成时间戳
# data = datetime(2019,12,30,18,35,40).timestamp()
# print(datetime.fromtimestamp(data))  # 时间戳转化为time
# # str 和 time 转化
# print("*"*10)
# date = datetime.strftime(datetime.now(),"%a,%b %d %H:%M")
# print(date)
# #str_datetime
# date_str = datetime.strptime("2019-12-30 18:35:40","%Y-%m-%d %H:%M:%S")
# print("*"*10)
# print(date_str)
# d=(x*x for x in range(10))
# def odd():
#  print('step 1')
#  yield 1
#  print('step 2')
#  yield(3)
#  print('step 3')
#  yield(5)
# d=odd()
# next(d)
# def _odd_iter():
#  n = 1
#  while True:
#    n = n + 2
#    yield n
# def _not_divisible(n):
#     return lambda x: x % n > 0
# def primes():
#  yield 2
#  it = _odd_iter() # 初始序列
#  while True:
#   n = next(it) # 返回序列的第一个数
#   yield n
#   it = filter(_not_divisible(n), it) # 构造新序列
# # 打印 1000 以内的素数:
# for n in primes():
#  if n < 10:
#    print(n)
#  else:
#    break
import  os
# data= os.listdir("G:\\")  #获取目前中全部的文件列表 返回的是【】
# print(data)
# print(os.path.splitext("G://siweifile//si_one.txt"))
# print(os.path.split("G://siweifile//si_one.txt"))
#os.mkdir("G://Test_File")
#os.mknod("G://Test_File//Test.txt")
with open("K:\\data.txt" ,"r+",encoding='gbk',errors='ignore') as f:
    data = f.read()
    print(data)
with open("G://Test_File//test.txt","a+")  as f:# 直接打开一个文件，如果文件不存在则创建文件
    f.write(data)















