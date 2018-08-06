import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='111111',
                       db='test',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

## create database
# try:
#     with conn.cursor() as cursor:
#         sql = 'CREATE DATABASE test'
#         cursor.execute(sql)
#     conn.commit()
# finally:
#     conn.close()

#create tables..

try:
    with conn.cursor() as cursor:
        sql = '''
            CREATE TABLE users (
                id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                email varchar(255) NOT NULL,
                password varchar(255) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8
'''
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()