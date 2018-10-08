import pymysql

#open database connection
#host, username, pass, db name
db = pymysql.connect("localhost", "root", "009564", "First")

#prepare a cursor object using cursor()
cursor = db.cursor()

#execute query using execute()
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone()
data = cursor.fetchone()
print ("database version is :%s" % data)

#disconnect from database
db.close()
