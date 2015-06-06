#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ == 'select test.db data'
#__author__ == 'ws'

import sqlite3 as sql
import logging as log
import logging.config
class Selsql(object):
      def __init__(self):
	 log.config.fileConfig('../../pylog/pylog.conf')
	 self.l = log.getLogger('simple')
       
      def ccs(self):
	 self.l.debug('connection test.db')
	 self.db = sql.connect('test.db');
     	 self.l.debug('connection test.db success') 
	 self.__cs = self.db.cursor()

      def closeAll(self):
	 self.db.commit()
	 if self.__cs != None:
		self.__cs.close()
	 if self.db != None:
		self.db.close()
	 
      def query(self):
         self.__cs.execute('select * from user where id=?','1')
         return self.__cs.fetchall()

      def queryAll(self):
	 self.__cs.execute("select * from user")
	 self.l.debug('apply rowcount:'+ str(self.__cs.rowcount))
	 return self.__cs.fetchall()

      def insert(self):
	 self.l.debug('insert data to test.db.table.user')
	 self.__cs.execute("insert into user values(?,?)",(3,'xl'))
         self.l.debug('insert data to test.db.table.user success')

      def upd(self):
         self.l.debug('upd data to test.db.table.user')
	 self.__cs.execute("update user set name='i love xl' where id=?",'1')	
	 self.l.debug('upd data to test.db.table.user') 

      def delete(self):
	 self.l.debug('del data to test.db.table.user')
	 self.__cs.execute("delete from user where id = ?", '3')
	 self.l.debug('del data to test.db.table.user')

if __name__ == '__main__': 
         s = Selsql()
	 s.ccs()
         #s.insert()
	 s.upd()
	 s.delete()
 	 data = s.queryAll()
         print(data)
         s.closeAll()
