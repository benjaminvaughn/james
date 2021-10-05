import mysql.connector

cnx = mysql.connector.connect(user='admin', password='rootrootroot',
                              host='database-1.ckitw0xkgkkg.us-west-2.rds.amazonaws.com',
                              port=3306)

cursor = cnx.cursor()

cursor.execute("USE pp")


cursor.execute("Select * from User")

cnx.close()