import pymysql

#open database connection
#host, username, pass, db name
db = pymysql.connect("localhost", "root", "009564", "First")

#prepare a cursor object using cursor()
cursor = db.cursor()

#sql query to insert a record into the database
sql = "INSERT INTO MyTable(ID,DATA) \
       VALUES (NULL,'%d')" % \
              (123)

try:   
    #execute query using execute()
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
#disconnect from database
db.close()
