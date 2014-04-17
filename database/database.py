import ConfigParser
import MySQLdb
def connect():
	cf=ConfigParser.ConfigParser()
	cf.read("config.db")
	host=cf.get("connection","host")
	port=cf.getint("connection","port")
	user=cf.get("connection","user")
	passwd=cf.get("connection","pass")
	try:
		print 'ok'
		conn=MySQLdb.connect(host=host,user=user,passwd=passwd,port=port)
		print conn
		return conn
	
	except Exception ,e:
		print "Mysql connection error:%s" % e 


def init():
	conn=connect()
	cur=conn.cursor()
	cur.execute('create database if not exists student2012;')
	
	conn.select_db('student2012')
	cur.execute('create table if not exists studentinfo(stuname char(255) not null,stuno char(255) not null,class char(255) not null)charset=gbk;')
	cur.execute('create table if not exists githubinfo(username char(255) not null,email char(255) not null)charset=gbk;')
	cur.execute('create table if not exists relation(stuno char(255) not null,email char(255) not null)charset=gbk;')
	cur.close()
	return conn


