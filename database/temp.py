import MySQLdb

try:
	conn=MySQLdb.connect('127.0.0.1','root','root',3306)
except Exception,e:
	print "error :%s" %e
