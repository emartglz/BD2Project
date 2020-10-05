import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="password")

c = db.cursor()
c.execute('CREATE DATABASE IF NOT EXISTS db')

db.close()