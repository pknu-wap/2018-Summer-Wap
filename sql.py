import pymysql

connect = pymysql.connect(host='root',
                          password = 'qwe123',
                          db = 'ict',
                          charset = 'utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)

sql = "SELECT * FROM ict WHRER id='adf'"

with connect.cursor() as cursor:
    cursor.excude(sql)