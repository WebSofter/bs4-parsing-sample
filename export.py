#Server Connection to MySQL:
import pymysql.cursors
import re
import time
#Vars of Opencart DB connect
dbHost = "remobser.bget.ru"
dbUser = "remobser_test"
dbPassword = "qvP78Xmm"
dbName = "remobser_test" 
dbCharset = 'utf8mb4'#'utf8'
dbInit =  'SET NAMES UTF8' 

# Connect to the database
connection = pymysql.connect(host=dbHost,
                             user=dbUser,
                             password=dbPassword,
                             db=dbName,
                             charset=dbCharset,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()