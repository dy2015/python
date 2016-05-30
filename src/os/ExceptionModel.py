'''
Created on 2016年5月29日

@author: dy
'''
#coding:utf-8
import MySQLdb
con=MySQLdb.connect(user='root',passwd='123',host='localhost')
con.select_db("mydatabase")
cu=con.cursor()
for g in cu.exectue("select * from studet"):
    print(g.fetchone())
con.commit()
cu.close()
con.close()
