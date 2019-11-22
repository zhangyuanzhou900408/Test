#xml.dom.* 模式解析xm
import xml.dom.minidom as  xmldom
import os
xmlfilepath = os.path.abspath("Test.xml")
print ("xml文件路径：", xmlfilepath)
# 得到文档对象
domobj = xmldom.parse(xmlfilepath)
print(domobj)
# 得到元素对象
elementobj = domobj.documentElement
print(elementobj)
#获得子标签1
subElementObj = elementobj.getElementsByTagName("login")
print(subElementObj)
print(subElementObj[0].getAttribute("username"))
print(subElementObj[0].getAttribute("passwd"))
print("--------------------------")
#获得子标签2
subElementObj2 = elementobj.getElementsByTagName("item")
for i in range(len(subElementObj2)):
    print(subElementObj2[i].getAttribute("id"))
subElementObj1 = elementobj.getElementsByTagName("caption")
for i in range(len(subElementObj1)):
    print("subElementObj1[i]:", type(subElementObj1[i]))
    print("subElementObj1[i]:", subElementObj1[i].firstChild.data)

from enum import Enum, unique
@unique #保障枚举类没有重复元素
class Weekday(Enum):
    Sun = 0  # Sun 的 value 被设定为 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Sun.value)
print("*"*20)
import  sqlite3
filepath = os.path.abspath("test.db")
if os.path.exists(filepath):
    os.remove(filepath)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行一条 SQL 语句，创建 user 表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score varchar(20))')
# 继续执行一条 SQL 语句，插入一条记录:
cursor.execute('insert into user (id, name, score) values (\'1\',\'Michael\',\"85\")')
cursor.close()
conn.commit()
conn.close()
conn = sqlite3.connect('test.db')
cursors = conn.cursor()
print(cursors.execute('select * from user where id=?', '1'))
value= cursors.fetchall()
print(value)
cursors.close()
conn.commit()
conn.close()


