# -*- coding:utf-8 -*-
# /use/dev/lib python3

__doc__ = '这是测试sqlite3con.py文件'
__author__ = 'ws'

#导入sqlite的驱动
import sys
import sqlite3 as sql3
import logging as log
import logging.config
class sqlc(object):
   def __init__(self):
	CONF_LOG = "../../pylog/pylog.conf"
     	log.config.fileConfig(CONF_LOG)
   	self.l = log.getLogger('simple')
   def createConn(self):
	#连接到sqlite database
	#数据库文件是test.db
	#如果文件不存在，会自动在当前目录创建
	self.l.info('create conn start')
	self._conn = sql3.connect('test.db')
	self.l.info('create conn end')
	#创建一个游标cursor
	self.__cs = self._conn.cursor()
   
   def closecon(self):
	self._conn.commit()#提交事物
	self._conn.close()#关闭连
	print('hasAttr:', self.__cs)
	if self.__cs != None:
	  self.__cs.close() #关闭游标接
	else:
 	  raise ValueError('__cs值不存在')

   def createT(self):
	self.__cs.execute('create table user (id varchar(20) primary key, name varchar(20))')

	self.__cs.execute('insert into user(id,name) values(\'1\', \'ws\')')
	#通过cursor获取受影响的行数
	print('插入数据的行数：',self.__cs.rowcount)
if __name__ == '__main__':
	db = sqlc()
	db.createConn()
#        db.createT()
#	db.closecon()

