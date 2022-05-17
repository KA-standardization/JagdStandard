import pymysql

conn = pymysql.connect(host='10.0.3.210', user='dgs', password='N2RiYTlkZWNm', database='dgs_zhihu',
                       charset='utf8mb4')

cursor = conn.cursor()

sql = ""
cursor.execute(sql)
conn.commit()
