import pymysql as mdb
#连接数据库
db = mdb.connect("localhost","root","root")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
#创建数据库
cursor.execute("CREATE DATABASE TestData")
print('Database version:', data)
#db.close()
#创建表及数据
sql_createTb = "CREATE TABLE `TestData`.`monkey`(`id` int(10) unsigned NOT NULL AUTO_INCREMENT,`LAST_NAME` char(10) NOT NULL,`AGE` int(10) unsigned NOT NULL,`SEX` char(10) NOT NULL,PRIMARY KEY (`id`)) ENGINE=MyISAM DEFAULT CHARSET=utf8"
sql_insert = "INSERT INTO `TestData`.`monkey`(LAST_NAME,AGE,SEX) VALUES('de2',18,'0')"
cursor.execute(sql_createTb)
cursor.execute(sql_insert)
print(cursor.rowcount)
db.commit()
cursor.close()
db.close()


